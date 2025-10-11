use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

struct Node {
    key: i32,
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
    prev: Option<Rc<RefCell<Node>>>,
}

struct LRUCache {
    capacity: i32,
    max_capacity: i32,
    hash_map: HashMap<i32, Rc<RefCell<Node>>>,
    head: Rc<RefCell<Node>>,
    tail: Rc<RefCell<Node>>,
}

fn insert_after(node: &Rc<RefCell<Node>>, new_node: &Rc<RefCell<Node>>) {
    let next_node = node.borrow().next.clone().unwrap();
    next_node.borrow_mut().prev = Some(new_node.clone());
    node.borrow_mut().next = Some(new_node.clone());

    new_node.borrow_mut().prev = Some(node.clone());
    new_node.borrow_mut().next = Some(next_node.clone());
}

fn delete_node(node: &Rc<RefCell<Node>>) {
    let next_node = node.borrow().next.clone().unwrap();
    let prev_node = node.borrow().prev.clone().unwrap();
    next_node.borrow_mut().prev = Some(prev_node.clone());
    prev_node.borrow_mut().next = Some(next_node.clone());
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {
    #[allow(dead_code)]
    fn new(capacity: i32) -> Self {
        let head = Node {
            key: 0,
            value: 0,
            next: None,
            prev: None,
        };
        let tail = Node {
            key: 0,
            value: 0,
            next: None,
            prev: None,
        };
        let cache = LRUCache {
            capacity: 0,
            max_capacity: capacity,
            hash_map: HashMap::new(),
            head: Rc::new(RefCell::new(head)),
            tail: Rc::new(RefCell::new(tail)),
        };

        cache.head.borrow_mut().next = Some(cache.tail.clone());
        cache.tail.borrow_mut().prev = Some(cache.head.clone());

        cache
    }

    #[allow(dead_code)]
    fn get(&self, key: i32) -> i32 {
        if let Some(node) = self.hash_map.get(&key) {
            delete_node(node);
            insert_after(&self.head, node);
        } else {
            return -1;
        }

        self.hash_map.get(&key).unwrap().borrow().value
    }

    #[allow(dead_code)]
    fn put(&mut self, key: i32, value: i32) {
        if self.max_capacity == 0 {
            return;
        }

        if let Some(node) = self.hash_map.get(&key) {
            delete_node(node);
            insert_after(&self.head, node);
            node.borrow_mut().value = value;
        } else {
            if self.capacity == self.max_capacity {
                let lru_node = self.tail.borrow().prev.clone().unwrap();
                self.hash_map.remove(&lru_node.borrow().key);
                delete_node(&lru_node);
                self.capacity -= 1;
            }
            let new_node = Rc::new(RefCell::new(Node {
                key,
                value,
                next: None,
                prev: None,
            }));
            insert_after(&self.head, &new_node);
            self.hash_map.insert(key, new_node);
            self.capacity += 1;
        }
    }
}
