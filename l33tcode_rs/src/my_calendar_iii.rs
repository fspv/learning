use std::collections::BTreeMap;

struct MyCalendarThree {
    map: BTreeMap<i32, i32>,
}

impl MyCalendarThree {
    #[allow(dead_code)]
    fn new() -> Self {
        Self {
            map: BTreeMap::new(),
        }
    }

    #[allow(dead_code)]
    fn book(&mut self, start_time: i32, end_time: i32) -> i32 {
        self.map
            .entry(start_time)
            .and_modify(|c| *c += 1)
            .or_insert(1);
        self.map
            .entry(end_time)
            .and_modify(|c| *c -= 1)
            .or_insert(-1);

        let mut max_k_booking = 0;
        let mut cur = 0;

        for delta in self.map.values() {
            cur += *delta;
            max_k_booking = max_k_booking.max(cur);
        }

        max_k_booking
    }
}
