#[allow(dead_code)]
struct Solution;

use std::collections::{HashSet, VecDeque};

fn rotate(string: &str, count: usize) -> String {
    let mut rotated_string = String::new();

    let chars: Vec<char> = string.chars().collect();

    for i in 0..chars.len() {
        rotated_string.push(chars[(i + count) % chars.len()]);
    }

    rotated_string
}

fn add_odd(string: &str, num: usize) -> String {
    let mut modified_string = String::new();

    let chars: Vec<char> = string.chars().collect();

    for (i, char) in chars.iter().enumerate() {
        match i {
            n if n % 2 == 0 => {
                modified_string.push(*char);
            }
            _ => {
                let mut num2 = char.to_digit(10).unwrap() as usize;
                num2 = (num2 + num) % 10;

                modified_string.push(num2.to_string().chars().find(|_| true).unwrap());
            }
        }
    }

    modified_string
}

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn find_lex_smallest_string(s: String, a: i32, b: i32) -> String {
        let mut queue = VecDeque::new();
        queue.push_back(s.to_string());

        let mut seen = HashSet::new();
        let mut min_string = s.to_string();

        while let Some(string) = queue.pop_front() {
            if string < min_string {
                min_string = string.to_string();
            }

            let rotated_string = rotate(&string, b.try_into().unwrap());
            let added_string = add_odd(&string, a.try_into().unwrap());

            if !seen.contains(&rotated_string) {
                seen.insert(rotated_string.clone());
                queue.push_back(rotated_string);
            }

            if !seen.contains(&added_string) {
                seen.insert(added_string.clone());
                queue.push_back(added_string);
            }
        }

        min_string
    }
}
