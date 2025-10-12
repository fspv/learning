#[allow(dead_code)]
pub struct Solution;

use std::char;

impl Solution {
    fn get_num(pos: usize, letters: &[char]) -> (usize, usize) {
        let mut out_pos = pos;
        let mut num = 0;
        while out_pos < letters.len() && letters[out_pos].is_ascii_digit() {
            num = num * 10 + letters[out_pos].to_digit(10).unwrap();
            out_pos += 1;
        }
        (out_pos, num.try_into().unwrap())
    }

    /// ```
    /// use l33tcode_rs::valid_word_abbreviation::Solution;
    /// assert_eq!(Solution::valid_word_abbreviation("".to_string(), "".to_string()), true);
    /// assert_eq!(Solution::valid_word_abbreviation("accb".to_string(), "a2b".to_string()), true);
    /// assert_eq!(Solution::valid_word_abbreviation("internationalization".to_string(), "i5a11o1".to_string()), true);
    /// assert_eq!(Solution::valid_word_abbreviation("a1b01c".to_string(), "abbxc".to_string()), false);
    /// ```
    /// # Panics
    /// It panics...
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn valid_word_abbreviation(word: String, abbr: String) -> bool {
        let letters: Vec<char> = word.chars().collect();
        let abbr_letters: Vec<char> = abbr.chars().collect();

        let mut pos_letters = 0;
        let mut pos_abbr = 0;

        while pos_abbr < abbr_letters.len() && pos_letters < letters.len() {
            if abbr_letters[pos_abbr].is_alphabetic() {
                if abbr_letters[pos_abbr] == letters[pos_letters] {
                    pos_abbr += 1;
                    pos_letters += 1;
                } else {
                    return false;
                }
            } else {
                if abbr_letters[pos_abbr].to_digit(10).unwrap() == 0 {
                    return false;
                }
                let (new_pos, num) = Self::get_num(pos_abbr, &abbr_letters);
                pos_abbr = new_pos;
                pos_letters += num;
            }
        }

        pos_abbr == abbr_letters.len() && pos_letters == letters.len()
    }
}
