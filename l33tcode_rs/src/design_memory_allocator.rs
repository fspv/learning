use std::collections::BTreeMap;
use std::collections::HashMap;

#[derive(Debug)]
struct Allocator {
    allocated: HashMap<i32, i32>,        // offset: size
    free: BTreeMap<i32, i32>,            // offset: size
    allocations: HashMap<i32, Vec<i32>>, // mid: [ptr]
}

#[allow(dead_code)]
impl Allocator {
    fn new(n: i32) -> Self {
        Self {
            allocated: HashMap::new(),
            free: BTreeMap::from([(0, n)]),
            allocations: HashMap::new(),
        }
    }

    fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        if let Some((&free_offset, &free_size)) = self.free.iter().find(|(_, s)| **s >= size) {
            self.free.remove(&free_offset);
            self.allocated.insert(free_offset, size);
            self.allocations.entry(m_id).or_default().push(free_offset);

            if free_size == size {
                return free_offset;
            }

            self.free.insert(free_offset + size, free_size - size);
            return free_offset;
        }

        -1
    }

    fn free_memory(&mut self, m_id: i32) -> i32 {
        let mut freed = 0;
        for ptr in self.allocations.remove(&m_id).unwrap_or_default() {
            if let Some(size) = self.allocated.remove(&ptr) {
                freed += size;
                self.free.insert(ptr, size);

                if let Some(&next_size) = self.free.get(&(ptr + size)) {
                    self.free.remove(&(ptr + size));
                    self.free.entry(ptr).and_modify(|v| *v += next_size);
                }

                if let Some((&prev_offset, &prev_size)) = self.free.range(..ptr).next_back()
                    && prev_offset + prev_size == ptr
                {
                    let size = self.free.remove(&ptr).unwrap();
                    self.free.entry(prev_offset).and_modify(|v| *v += size);
                }
            }
        }

        freed
    }
}
