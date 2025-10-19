use std::cell::RefCell;
use std::rc::Rc;
use std::{collections::HashMap, fmt::Debug};

struct Version<V: Clone + Debug> {
    value: Option<V>,
    // The transaction id which created this row (similar to xmin in postgres)
    tx_id_created: usize,
    // The transaction id which deleted this row or created a new version of the row (similar to
    // xmax in postgres)
    tx_id_deleted: usize,
}

#[derive(Debug, PartialEq, Eq)]
enum TransactionStatus {
    Active,
    Committed,
    Aborted,
}

struct Transaction {
    id: usize,
    status: TransactionStatus,
}

struct DB<V: Clone + Debug> {
    // Updating fields below is not currently thread safe, there should be a mutex on store
    // modifications or we should use some lock-free techniques
    store: HashMap<String, Vec<Rc<RefCell<Version<V>>>>>,
    transactions: HashMap<usize, Transaction>,
    latest_tx_id: usize,
}

impl<V> DB<V>
where
    V: Clone + Debug,
{
    // Get returns a version of a value, which can then be later used in set to create a new
    // version
    fn get(&self, key: &str, tx_id: usize) -> Option<Rc<RefCell<Version<V>>>> {
        // TODO: allow to get without a transaction to avoid incrementing tx_id every time

        if let Some(transaction) = self.transactions.get(&tx_id) {
            assert!(
                transaction.status == TransactionStatus::Active,
                "transaction is not active"
            );
        }

        if let Some(versions) = self.store.get(key) {
            // Iterate in reverse order to find the latest known version. The assumption is that
            // the versions are sorted by the tx_id_created, because we don't have complex page
            // layout and just append entries to the versions list. Also, there is no GC, so
            // versions are never deleted
            for version in versions.iter().rev() {
                // If there is a value version created in this transaction, return it
                if version.borrow().tx_id_created == tx_id {
                    if version.borrow().tx_id_deleted == 0 {
                        return Some(version.clone());
                    }
                    return None;
                }

                // Implement READ COMMITTED semantics if the value has not been updated in this
                // transaction
                let transaction = self
                    .transactions
                    .get(&version.borrow().tx_id_created)
                    .unwrap();
                if transaction.status == TransactionStatus::Committed {
                    // If deleted by a commited transaction, return None
                    if version.borrow_mut().tx_id_deleted != 0 {
                        let transaction_deleted = self
                            .transactions
                            .get(&version.borrow().tx_id_deleted)
                            .unwrap();
                        if transaction_deleted.status == TransactionStatus::Committed {
                            return None;
                        }
                    }
                    return Some(version.clone());
                }
            }
        }

        None
    }

    // Assumes that the key exists
    // Previous version is the version of the string we're going to modify. We can obtain it using
    // the get method
    fn update(
        &mut self,
        key: &str,
        value: V,
        tx_id: usize,
        prev_version: &Rc<RefCell<Version<V>>>,
    ) {
        let tx_id_deleted = prev_version.borrow().tx_id_deleted;
        assert!(
            tx_id_deleted == 0,
            "Serialisation error in {tx_id}: the row {key} has been deleted by {tx_id_deleted}"
        );

        prev_version.borrow_mut().tx_id_deleted = tx_id;
        let version = Version {
            value: Some(value),
            tx_id_created: tx_id,
            tx_id_deleted: 0,
        };

        self.store
            .get_mut(key)
            .unwrap()
            .push(Rc::new(RefCell::new(version)));
    }

    fn delete(&mut self, tx_id: usize, prev_version: &Rc<RefCell<Version<V>>>) {
        let tx_id_deleted = prev_version.borrow().tx_id_deleted;
        assert!(
            tx_id_deleted == 0,
            "Serialisation error in {tx_id}: the row has been deleted by {tx_id_deleted}"
        );

        prev_version.borrow_mut().tx_id_deleted = tx_id;
    }

    fn insert(&mut self, key: &str, value: V, tx_id: usize) {
        let version = Version {
            value: Some(value),
            tx_id_created: tx_id,
            tx_id_deleted: 0,
        };

        self.store
            .entry(key.to_string())
            .or_default()
            .push(Rc::new(RefCell::new(version)));
    }

    fn begin(&mut self) -> usize {
        self.latest_tx_id += 1;

        self.transactions.insert(
            self.latest_tx_id,
            Transaction {
                id: self.latest_tx_id,
                status: TransactionStatus::Active,
            },
        );

        self.latest_tx_id
    }

    fn commit(&mut self, tx_id: usize) {
        if let Some(transaction) = self.transactions.get_mut(&tx_id) {
            assert!(
                transaction.status == TransactionStatus::Active,
                "Transaction {tx_id} as already been finished",
            );

            transaction.status = TransactionStatus::Committed;
        } else {
            panic!("Transaction {tx_id} doesn't exist");
        }
    }

    fn rollback(&mut self, tx_id: usize) {
        if let Some(transaction) = self.transactions.get_mut(&tx_id) {
            assert!(
                transaction.status == TransactionStatus::Active,
                "Transaction {tx_id} as already been finished",
            );

            transaction.status = TransactionStatus::Aborted;
        } else {
            panic!("Transaction {tx_id} doesn't exist");
        }
    }
}
