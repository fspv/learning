#[allow(dead_code)]
pub struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut num_bottles = num_bottles;
        let mut num_exchange = num_exchange;
        let mut num_empty = 0;

        let mut res = 0;

        while num_bottles + num_empty >= num_exchange {
            num_empty += num_bottles;
            res += num_bottles;
            num_bottles = 0;

            num_empty -= num_exchange;
            num_bottles += 1;
            num_exchange += 1;
        }

        res + num_bottles
    }
}
