use std::collections::HashMap;

struct TrieNode {
    children: HashMap<char, Box<TrieNode>>,
    leaf: bool,
}
struct MagicDictionary {
    trie_root: Box<TrieNode>,
}

fn insert_trie(node: &mut Box<TrieNode>, word: &Vec<char>, pos: usize) {
    if pos == word.len() {
        node.leaf = true;
        return;
    }

    if let Some(child_node) = node.children.get_mut(&word[pos]) {
        insert_trie(child_node, word, pos + 1);
    } else {
        let mut child_node = Box::new(TrieNode {
            children: HashMap::new(),
            leaf: false,
        });
        insert_trie(&mut child_node, word, pos + 1);
        node.children.insert(word[pos], child_node);
    }
}

fn search_trie_with_one_change(
    node: &TrieNode,
    word: &Vec<char>,
    pos: usize,
    can_change: bool,
) -> bool {
    if pos == word.len() {
        return !can_change && node.leaf;
    }

    if let Some(child_node) = node.children.get(&word[pos]) {
        if search_trie_with_one_change(child_node, word, pos + 1, can_change) {
            return true;
        }
    }

    if can_change {
        for (char, child_node) in &node.children {
            if *char != word[pos] {
                if search_trie_with_one_change(child_node, word, pos + 1, false) {
                    return true;
                }
            }
        }
    }

    false
}

impl MagicDictionary {
    #[allow(dead_code)]
    fn new() -> Self {
        MagicDictionary {
            trie_root: Box::new(TrieNode {
                children: HashMap::new(),
                leaf: false,
            }),
        }
    }

    #[allow(dead_code, clippy::needless_pass_by_value)]
    fn build_dict(&mut self, dictionary: Vec<String>) {
        for word in dictionary {
            insert_trie(&mut self.trie_root, &word.chars().collect(), 0);
        }
    }

    #[allow(dead_code, clippy::needless_pass_by_value)]
    fn search(&self, search_word: String) -> bool {
        search_trie_with_one_change(&self.trie_root, &search_word.chars().collect(), 0, true)
    }
}
