use std::collections::HashMap;

#[derive(Debug)]
struct SnapshotArray {
    snapshot: i32,
    data: HashMap<i32, Vec<(i32, i32)>>,
}

#[allow(dead_code)]
impl SnapshotArray {
    fn new(length: i32) -> Self {
        let mut x = Self {
            data: HashMap::new(),
            snapshot: 0,
        };
        for i in 0..length {
            x.data.insert(i, vec![(0, 0)]);
        }

        x
    }

    fn set(&mut self, index: i32, val: i32) {
        self.data.entry(index).and_modify(|e| {
            if let Some(last) = e.iter().last() {
                if last.0 == self.snapshot {
                    let len = e.len() - 1;
                    e[len] = (self.snapshot, val);
                } else {
                    e.push((self.snapshot, val));
                }
            }
        });
    }

    fn snap(&mut self) -> i32 {
        self.snapshot += 1;

        self.snapshot - 1
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        if let Some(versions) = self.data.get(&index) {
            let (mut left, mut right) = (0, versions.len());

            while left < right {
                let mid = left + (right - left) / 2;
                if versions[mid].0 <= snap_id {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            return versions[left - 1].1;
        }

        0
    }
}
