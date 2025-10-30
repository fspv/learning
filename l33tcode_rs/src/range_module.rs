use std::collections::BTreeMap;

#[allow(dead_code)]
#[derive(Debug)]
struct RangeModule {
    // Assume start != end, or in other words empty intervals are not permitted
    map: BTreeMap<i32, i32>, // start: end
}

impl RangeModule {
    #[allow(dead_code)]
    fn new() -> Self {
        Self {
            map: BTreeMap::new(),
        }
    }

    #[allow(dead_code)]
    fn find_overlapping(&self, left: i32, right: i32) -> Vec<(i32, i32)> {
        let mut overlapping = Vec::new();

        for (start, end) in self.map.range(..=right).rev() {
            if *end < left {
                break;
            }
            overlapping.push((*start, *end));
        }

        overlapping
    }

    #[allow(dead_code)]
    fn add_range(&mut self, left: i32, right: i32) {
        let mut min_start = left;
        let mut max_end = right;

        for (start, end) in self.find_overlapping(left, right) {
            max_end = max_end.max(end);
            min_start = min_start.min(start);
            self.map.remove(&start);
        }

        self.map.insert(min_start, max_end);
    }

    #[allow(dead_code)]
    fn query_range(&self, left: i32, right: i32) -> bool {
        for (start, end) in self.find_overlapping(left, right) {
            if start <= left && right <= end {
                return true;
            }
        }
        false
    }

    #[allow(dead_code)]
    fn remove_range(&mut self, left: i32, right: i32) {
        for (start, end) in self.find_overlapping(left, right) {
            self.map.remove(&start);

            if left <= start && start <= right && right <= end {
                if right != end {
                    self.map.insert(right, end);
                }
            } else if start <= left && left <= end && end <= right {
                if start != left {
                    self.map.insert(start, left);
                }
            } else if start <= left && left <= right && right <= end {
                if start != left {
                    self.map.insert(start, left);
                }
                if right != end {
                    self.map.insert(right, end);
                }
            }
        }
    }
}
