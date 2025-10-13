#[allow(dead_code)]
struct Solution;

use std::collections::HashMap;

fn dfs(
    string: &String,
    hash_counter: &mut HashMap<u64, u64>,
    hashes: &mut Vec<u64>,
    word_len: usize,
    pos: usize,
    total: &mut usize,
) -> bool {
    if *total == 0 {
        return true;
    }

    if pos >= string.len() {
        return false;
    }

    if *hash_counter.get(&hashes[pos]).unwrap_or(&0) > 0 {
        hash_counter.entry(hashes[pos]).and_modify(|e| *e -= 1);
        *total -= 1;

        if dfs(
            string,
            hash_counter,
            hashes,
            word_len,
            pos + word_len,
            total,
        ) {
            hash_counter.entry(hashes[pos]).and_modify(|e| *e += 1);
            *total += 1;
            return true;
        }
        hash_counter.entry(hashes[pos]).and_modify(|e| *e += 1);
        *total += 1;
    }

    false
}

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        // TODO: some of the test cases are still failing
        // Identical python solution works, but this is probably due to the fact that python has
        // unbound integers
        if words.is_empty() {
            return vec![];
        }
        let word_len = words[0].len();
        let mut hashes = vec![0; s.len()];

        let chars_to_num: Vec<u64> = s.chars().map(|c| (c as u64) - ('a' as u64)).collect();

        let mut hash = 0_u64;

        for pos in 0..=s.len() {
            if pos >= word_len {
                hashes[pos - word_len] = hash;
            }

            if pos < s.len() {
                hash = hash.wrapping_mul(26).wrapping_add(chars_to_num[pos]);
            }

            if pos >= word_len {
                hash %= 26_u64.saturating_pow(word_len.try_into().unwrap());
            }
        }

        let mut hash_counter = HashMap::new();

        for word in &words {
            let mut hash = 0;

            for c in word.chars() {
                hash = hash * 26 + (c as u64) - ('a' as u64);
            }
            hash_counter
                .entry(hash)
                .and_modify(|e| *e += 1)
                .or_insert(1);
        }

        let mut result = Vec::new();

        #[allow(clippy::range_plus_one)]
        for pos in 0..(s.len() - word_len * words.len() + 1) {
            let mut total = words.len();
            if dfs(
                &s,
                &mut hash_counter,
                &mut hashes,
                word_len,
                pos,
                &mut total,
            ) {
                result.push(i32::try_from(pos).unwrap());
            }
        }

        result
    }
}
