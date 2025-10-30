use std::{cell::RefCell, collections::HashMap, rc::Rc};

struct Block {
    offset: i32,
    size: i32,
    prev: Option<Rc<RefCell<Block>>>,
    next: Option<Rc<RefCell<Block>>>,
}
struct Allocator {
    size: i32,
    head: Rc<RefCell<Block>>,
    allocations: HashMap<i32, Vec<Rc<RefCell<Block>>>>,
}

fn find_gap(node: &Rc<RefCell<Block>>, size: i32) -> Option<Rc<RefCell<Block>>> {
    let mut cur: Option<Rc<RefCell<Block>>> = Some(node.clone());

    while let Some(prev) = cur {
        if let Some(next) = prev.borrow().next.clone() {
            let gap = next.borrow().offset - (prev.borrow().offset + prev.borrow().size);

            if gap >= size {
                return Some(prev.clone());
            }
        }

        cur = prev.borrow().next.clone();
    }

    None
}

fn delete_block(node: &Rc<RefCell<Block>>) {
    let prev = node.borrow().prev.clone().unwrap();
    let next = node.borrow().next.clone().unwrap();

    prev.borrow_mut().next = Some(next);

    let next = node.borrow().next.clone().unwrap();
    next.borrow_mut().prev = Some(prev);
}

#[allow(dead_code)]
impl Allocator {
    fn new(n: i32) -> Self {
        let tail = Rc::new(RefCell::new(Block {
            size: 0,
            offset: n,
            prev: None,
            next: None,
        }));
        let head = Rc::new(RefCell::new(Block {
            size: 0,
            offset: 0,
            prev: None,
            next: None,
        }));

        head.borrow_mut().next = Some(tail.clone());
        tail.borrow_mut().prev = Some(head.clone());

        Allocator {
            size: n,
            head,
            allocations: HashMap::new(),
        }
    }

    fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        println!("allocate {size} {m_id}");
        if let Some(prev_block) = find_gap(&self.head, size) {
            let offset = prev_block.borrow().offset + prev_block.borrow().size;
            let next_block = prev_block.borrow().next.clone().unwrap();
            let new_block = Rc::new(RefCell::new(Block {
                offset,
                size,
                prev: Some(prev_block.clone()),
                next: Some(next_block.clone()),
            }));
            let next_block = prev_block.borrow().next.clone().unwrap();
            prev_block.borrow_mut().next = Some(new_block.clone());
            next_block.borrow_mut().prev = Some(new_block.clone());

            self.allocations
                .entry(m_id)
                .or_default()
                .push(new_block.clone());

            return offset;
        }

        -1
    }

    fn free_memory(&mut self, m_id: i32) -> i32 {
        println!("free_memory {m_id}");
        let mut freed = 0;
        if let Some(blocks) = self.allocations.remove(&m_id) {
            for block in blocks {
                println!(
                    "found block at offset {} with size {}",
                    block.borrow().offset,
                    block.borrow().size
                );
                freed += block.borrow().size;
                delete_block(&block);
            }
        }

        freed
    }
}
