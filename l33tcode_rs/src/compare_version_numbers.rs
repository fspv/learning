#[allow(dead_code)]
pub struct Solution;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let mut iter1 = version1.split('.').map(|s| s.parse::<i32>().unwrap());
        let mut iter2 = version2.split('.').map(|s| s.parse::<i32>().unwrap());

        loop {
            let v1 = iter1.next();
            let v2 = iter2.next();

            match (v1, v2) {
                (None, None) => return 0,
                (None, Some(n)) => {
                    if n > 0 {
                        return -1;
                    }
                }
                (Some(n), None) => {
                    if n > 0 {
                        return 1;
                    }
                }
                (Some(n1), Some(n2)) => {
                    if n1 < n2 {
                        return -1;
                    }
                    if n1 > n2 {
                        return 1;
                    }
                }
            }
        }
    }
}
