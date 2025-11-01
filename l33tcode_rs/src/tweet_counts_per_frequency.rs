use std::collections::{BTreeMap, HashMap};

#[derive(Debug)]
struct TweetCounts {
    map: HashMap<String, BTreeMap<i32, i32>>,
}

impl TweetCounts {
    #[allow(dead_code)]
    fn new() -> Self {
        Self {
            map: HashMap::new(),
        }
    }

    #[allow(dead_code)]
    fn record_tweet(&mut self, tweet_name: String, time: i32) {
        self.map
            .entry(tweet_name)
            .or_default()
            .entry(time)
            .and_modify(|c| *c += 1)
            .or_insert(1);
    }

    #[allow(dead_code, clippy::needless_pass_by_value)]
    fn get_tweet_counts_per_frequency(
        &self,
        freq: String,
        tweet_name: String,
        start_time: i32,
        end_time: i32,
    ) -> Vec<i32> {
        let counts = self.map.get(&tweet_name).unwrap();

        let delta = match &freq[..] {
            "second" => 1,
            "minute" => 60,
            "hour" => 3600,
            "day" => 86400,
            _ => panic!("fail"),
        };

        let mut res = vec![];

        let mut iter = counts.range(start_time..=end_time).peekable();

        let mut cur_time = end_time.min(start_time + delta - 1);

        while cur_time <= end_time {
            let mut total_count = 0;
            while let Some((time, count)) = iter.peek() {
                if **time <= cur_time {
                    total_count += **count;
                    iter.next();
                } else {
                    break;
                }
            }
            res.push(total_count);
            if cur_time + delta > end_time && cur_time != end_time {
                cur_time = end_time;
            } else {
                cur_time += delta;
            }
        }

        res
    }
}
