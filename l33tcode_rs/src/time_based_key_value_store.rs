use std::collections::HashMap;

struct TimeMap {
    // key -> Vec<(timestamp, value)>
    storage: HashMap<String, Vec<(i32, String)>>,
}

impl TimeMap {
    #[allow(dead_code)]
    fn new() -> Self {
        Self {
            storage: HashMap::new(),
        }
    }

    #[allow(dead_code, clippy::needless_pass_by_value)]
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        let timeline = self.storage.entry(key).or_default();
        let partition_point = timeline.partition_point(|x| x.0 < timestamp);
        if partition_point == timeline.len() {
            timeline.push((timestamp, value));
        } else if timeline[partition_point].0 == timestamp {
            timeline[partition_point].1 = value;
        } else {
            timeline.insert(partition_point, (timestamp, value));
        }
    }

    #[allow(dead_code, clippy::needless_pass_by_value)]
    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(timeline) = self.storage.get(&key) {
            let partition_point = timeline.partition_point(|x| x.0 <= timestamp);
            if partition_point == 0 {
                return String::new();
            }

            return timeline[partition_point - 1].1.clone();
        }

        String::new()
    }
}
