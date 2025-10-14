#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn is_palindrome(x: i32) -> bool {
        if x != 0 && x % 10 == 0 {
            return false;
        }

        let mut inverted = 0;
        let mut num = x;

        while num > 0 {
            inverted *= 10;
            inverted += num % 10;
            num /= 10;
        }

        x == inverted
    }
}
