#[allow(dead_code)]
struct Solution;

use std::collections::HashMap;

fn dfs(
    string_pos: usize,
    pattern_pos: usize,
    string: &Vec<char>,
    pattern: &Vec<char>,
    cache: &mut HashMap<(usize, usize), bool>,
) -> bool {
    if let Some(cached) = cache.get(&(string_pos, pattern_pos)) {
        return *cached;
    }

    if string_pos == string.len() || pattern_pos == pattern.len() {
        if pattern.get(pattern_pos + 1) == Some(&'*') {
            return dfs(string_pos, pattern_pos + 2, string, pattern, cache);
        }

        return string_pos == string.len() && pattern_pos == pattern.len();
    }

    let mut result = false;

    match pattern.get(pattern_pos) {
        Some('.') => match pattern.get(pattern_pos + 1) {
            Some('*') => {
                result = result
                    || dfs(string_pos + 1, pattern_pos + 2, string, pattern, cache)
                    || dfs(string_pos + 1, pattern_pos, string, pattern, cache)
                    || dfs(string_pos, pattern_pos + 2, string, pattern, cache);
            }
            _ => {
                result = result || dfs(string_pos + 1, pattern_pos + 1, string, pattern, cache);
            }
        },
        _ => match pattern.get(pattern_pos + 1) {
            Some('*') => {
                if string[string_pos] == pattern[pattern_pos] {
                    result = result
                        || dfs(string_pos + 1, pattern_pos + 2, string, pattern, cache)
                        || dfs(string_pos + 1, pattern_pos, string, pattern, cache)
                        || dfs(string_pos, pattern_pos + 2, string, pattern, cache);
                } else {
                    result = result || dfs(string_pos, pattern_pos + 2, string, pattern, cache);
                }
            }
            _ => {
                if string[string_pos] == pattern[pattern_pos] {
                    result = result || dfs(string_pos + 1, pattern_pos + 1, string, pattern, cache);
                }
            }
        },
    }

    cache.insert((string_pos, pattern_pos), result);

    result
}

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn is_match(s: String, p: String) -> bool {
        let mut cache: HashMap<(usize, usize), bool> = HashMap::new();
        dfs(0, 0, &s.chars().collect(), &p.chars().collect(), &mut cache)
    }
}
