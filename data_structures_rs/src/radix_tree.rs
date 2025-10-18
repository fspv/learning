use std::collections::HashMap;
use std::fmt::Debug;

#[derive(Debug)]
struct TreeNode<V: Clone + Debug> {
    children: HashMap<String, TreeNode<V>>,
    value: Option<V>,
}

struct RadixTree<V: Clone + Debug> {
    tree_root: TreeNode<V>,
}

impl<V> Default for RadixTree<V>
where
    V: Clone + Debug,
{
    fn default() -> Self {
        Self {
            tree_root: TreeNode {
                children: HashMap::new(),
                value: None,
            },
        }
    }
}

fn insert_radix_tree<V: Clone + Debug>(node: &mut TreeNode<V>, key: &str, value: V) {
    if key.is_empty() {
        node.value = Some(value);
        return;
    }

    if let Some(child_key) = node
        .children
        .keys()
        .find(|child_key| child_key.chars().next() == key.chars().next())
        .cloned()
    {
        let common_prefix_length = child_key
            .chars()
            .zip(key.chars())
            .take_while(|(a, b)| a == b)
            .count();

        if common_prefix_length == child_key.len() {
            insert_radix_tree(
                node.children.get_mut(&child_key).unwrap(),
                &key[common_prefix_length..],
                value,
            );
            return;
        } else if common_prefix_length > 0 {
            // If partial key match found, split the path
            let child_node = node.children.remove(&child_key).unwrap();
            let mut split_node = TreeNode {
                value: None,
                children: HashMap::from([(
                    child_key[common_prefix_length..].to_string(),
                    child_node,
                )]),
            };

            if common_prefix_length == key.len() {
                split_node.value = Some(value);
            } else {
                split_node.children.insert(
                    key[common_prefix_length..].to_string(),
                    TreeNode {
                        value: Some(value),
                        children: HashMap::new(),
                    },
                );
            }

            node.children
                .insert(key[..common_prefix_length].to_string(), split_node);

            return;
        }
        return;
    }

    // If nothing found, insert a new node
    let next_node = TreeNode {
        children: HashMap::new(),
        value: Some(value),
    };
    node.children.insert(key.to_string(), next_node);
}

fn get_radix_tree<V: Clone + Debug>(node: &TreeNode<V>, key: &str) -> Option<V> {
    if key.is_empty() {
        return node.value.clone();
    }

    node.children
        .iter()
        .find(|(child_key, _)| key.starts_with(*child_key))
        .and_then(|(child_key, child_node)| get_radix_tree(child_node, &key[child_key.len()..]))
}

fn delete_radix_tree<V: Clone + Debug>(node: &mut TreeNode<V>, key: &str) -> bool {
    if key.is_empty() {
        node.value = None;
        return node.children.is_empty();
    }

    let matching_key = node
        .children
        .keys()
        .find(|child_key| key.starts_with(*child_key))
        .cloned();

    if let Some(child_key) = matching_key {
        if delete_radix_tree(
            node.children.get_mut(&child_key).unwrap(),
            &key[child_key.len()..],
        ) {
            node.children.remove(&child_key);
        }
    }

    if node.value.is_none() && node.children.len() == 1 {
        let (child_key, child_node) = node.children.drain().next().unwrap();
        if child_node.children.len() == 1 && child_node.value.is_none() {
            let (grandchild_key, grandchild) = child_node.children.into_iter().next().unwrap();
            node.children
                .insert(format!("{child_key}{grandchild_key}"), grandchild);
        } else {
            node.children.insert(child_key, child_node);
        }
    }

    node.value.is_none() && node.children.is_empty()
}

fn count_values<V: Clone + Debug>(node: &TreeNode<V>) -> usize {
    let mut count = usize::from(node.value.is_some());
    for child in node.children.values() {
        count += count_values(child);
    }
    count
}

impl<V> RadixTree<V>
where
    V: Clone + Debug,
{
    #[allow(dead_code)]
    pub fn new() -> Self {
        RadixTree::default()
    }

    #[allow(dead_code)]
    pub fn insert(&mut self, key: &str, value: V) {
        insert_radix_tree(&mut self.tree_root, key, value);
    }

    #[allow(dead_code)]
    pub fn get(&self, key: &str) -> Option<V> {
        get_radix_tree(&self.tree_root, key)
    }

    #[allow(dead_code)]
    pub fn delete(&mut self, key: &str) {
        delete_radix_tree(&mut self.tree_root, key);
    }

    #[allow(dead_code)]
    pub fn len(&self) -> usize {
        count_values(&self.tree_root)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashMap;

    // Helper function to create a new RadixTree
    fn create_tree() -> RadixTree<String> {
        RadixTree {
            tree_root: TreeNode {
                children: HashMap::new(),
                value: None,
            },
        }
    }

    #[test]
    fn test_insert_and_get_single_key() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());
        assert_eq!(tree.get("hello"), Some("world".to_string()));
    }

    #[test]
    fn test_insert_and_get_multiple_keys() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());
        tree.insert("hi", "there".to_string());
        tree.insert("hey", "you".to_string());

        assert_eq!(tree.get("hello"), Some("world".to_string()));
        assert_eq!(tree.get("hi"), Some("there".to_string()));
        assert_eq!(tree.get("hey"), Some("you".to_string()));
    }

    #[test]
    fn test_get_nonexistent_key() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());
        assert_eq!(tree.get("hi"), None);
        assert_eq!(tree.get("hell"), None);
        assert_eq!(tree.get("hello!"), None);
    }

    #[test]
    fn test_insert_keys_with_common_prefix() {
        let mut tree = create_tree();
        tree.insert("test", "1".to_string());
        tree.insert("testing", "2".to_string());
        tree.insert("tested", "3".to_string());
        tree.insert("tester", "4".to_string());

        assert_eq!(tree.get("test"), Some("1".to_string()));
        assert_eq!(tree.get("testing"), Some("2".to_string()));
        assert_eq!(tree.get("tested"), Some("3".to_string()));
        assert_eq!(tree.get("tester"), Some("4".to_string()));
    }

    #[test]
    fn test_insert_overlapping_keys() {
        let mut tree = create_tree();
        tree.insert("car", "1".to_string());
        tree.insert("card", "2".to_string());
        tree.insert("cards", "3".to_string());
        tree.insert("care", "4".to_string());
        tree.insert("careful", "5".to_string());

        assert_eq!(tree.get("car"), Some("1".to_string()));
        assert_eq!(tree.get("card"), Some("2".to_string()));
        assert_eq!(tree.get("cards"), Some("3".to_string()));
        assert_eq!(tree.get("care"), Some("4".to_string()));
        assert_eq!(tree.get("careful"), Some("5".to_string()));
    }

    #[test]
    fn test_update_existing_key() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());
        assert_eq!(tree.get("hello"), Some("world".to_string()));

        tree.insert("hello", "universe".to_string());
        assert_eq!(tree.get("hello"), Some("universe".to_string()));
    }

    #[test]
    fn test_empty_key() {
        let mut tree = create_tree();
        tree.insert("", "empty".to_string());
        assert_eq!(tree.get(""), Some("empty".to_string()));
    }

    #[test]
    fn test_single_character_keys() {
        let mut tree = create_tree();
        tree.insert("a", "1".to_string());
        tree.insert("b", "2".to_string());
        tree.insert("c", "3".to_string());

        assert_eq!(tree.get("a"), Some("1".to_string()));
        assert_eq!(tree.get("b"), Some("2".to_string()));
        assert_eq!(tree.get("c"), Some("3".to_string()));
    }

    #[test]
    fn test_unicode_keys() {
        let mut tree = create_tree();
        tree.insert("café", "coffee".to_string());
        tree.insert("naïve", "simple".to_string());
        tree.insert("日本", "Japan".to_string());
        tree.insert("🎉", "party".to_string());

        assert_eq!(tree.get("café"), Some("coffee".to_string()));
        assert_eq!(tree.get("naïve"), Some("simple".to_string()));
        assert_eq!(tree.get("日本"), Some("Japan".to_string()));
        assert_eq!(tree.get("🎉"), Some("party".to_string()));
    }

    #[test]
    fn test_long_keys() {
        let mut tree = create_tree();
        let long_key = "a".repeat(1000);
        let another_long_key = "b".repeat(1000);

        tree.insert(&long_key, "long_value".to_string());
        tree.insert(&another_long_key, "another_long_value".to_string());

        assert_eq!(tree.get(&long_key), Some("long_value".to_string()));
        assert_eq!(
            tree.get(&another_long_key),
            Some("another_long_value".to_string())
        );
    }

    #[test]
    fn test_keys_with_special_characters() {
        let mut tree = create_tree();
        tree.insert("hello-world", "1".to_string());
        tree.insert("hello_world", "2".to_string());
        tree.insert("hello.world", "3".to_string());
        tree.insert("hello world", "4".to_string());
        tree.insert("hello/world", "5".to_string());

        assert_eq!(tree.get("hello-world"), Some("1".to_string()));
        assert_eq!(tree.get("hello_world"), Some("2".to_string()));
        assert_eq!(tree.get("hello.world"), Some("3".to_string()));
        assert_eq!(tree.get("hello world"), Some("4".to_string()));
        assert_eq!(tree.get("hello/world"), Some("5".to_string()));
    }

    #[test]
    fn test_numeric_string_keys() {
        let mut tree = create_tree();
        tree.insert("123", "numeric".to_string());
        tree.insert("1234", "longer_numeric".to_string());
        tree.insert("12", "shorter_numeric".to_string());

        assert_eq!(tree.get("123"), Some("numeric".to_string()));
        assert_eq!(tree.get("1234"), Some("longer_numeric".to_string()));
        assert_eq!(tree.get("12"), Some("shorter_numeric".to_string()));
    }

    #[test]
    fn test_insert_many_keys_stress() {
        let mut tree = create_tree();
        let n = 100;

        // Insert many keys
        for i in 0..n {
            let key = format!("key_{i}");
            let value = format!("value_{i}");
            tree.insert(&key, value);
        }

        // Verify all keys are retrievable
        for i in 0..n {
            let key = format!("key_{i}");
            let expected_value = format!("value_{i}");
            assert_eq!(tree.get(&key), Some(expected_value));
        }
    }

    #[test]
    fn test_hierarchical_keys() {
        let mut tree = create_tree();
        tree.insert("users", "all_users".to_string());
        tree.insert("users/john", "john_data".to_string());
        tree.insert("users/john/profile", "john_profile".to_string());
        tree.insert("users/jane", "jane_data".to_string());
        tree.insert("users/jane/settings", "jane_settings".to_string());

        assert_eq!(tree.get("users"), Some("all_users".to_string()));
        assert_eq!(tree.get("users/john"), Some("john_data".to_string()));
        assert_eq!(
            tree.get("users/john/profile"),
            Some("john_profile".to_string())
        );
        assert_eq!(tree.get("users/jane"), Some("jane_data".to_string()));
        assert_eq!(
            tree.get("users/jane/settings"),
            Some("jane_settings".to_string())
        );
    }

    #[test]
    fn test_similar_keys_different_lengths() {
        let mut tree = create_tree();
        tree.insert("a", "1".to_string());
        tree.insert("aa", "2".to_string());
        tree.insert("aaa", "3".to_string());
        tree.insert("aaaa", "4".to_string());

        assert_eq!(tree.get("a"), Some("1".to_string()));
        assert_eq!(tree.get("aa"), Some("2".to_string()));
        assert_eq!(tree.get("aaa"), Some("3".to_string()));
        assert_eq!(tree.get("aaaa"), Some("4".to_string()));
        assert_eq!(tree.get("aaaaa"), None);
    }

    #[test]
    fn test_keys_that_are_prefixes() {
        let mut tree = create_tree();
        // Insert longer key first
        tree.insert("testing", "long".to_string());
        tree.insert("test", "short".to_string());

        assert_eq!(tree.get("test"), Some("short".to_string()));
        assert_eq!(tree.get("testing"), Some("long".to_string()));

        // Now in reverse order
        let mut tree2 = create_tree();
        tree2.insert("test", "short".to_string());
        tree2.insert("testing", "long".to_string());

        assert_eq!(tree2.get("test"), Some("short".to_string()));
        assert_eq!(tree2.get("testing"), Some("long".to_string()));
    }

    #[test]
    fn test_case_sensitivity() {
        let mut tree = create_tree();
        tree.insert("Hello", "1".to_string());
        tree.insert("hello", "2".to_string());
        tree.insert("HELLO", "3".to_string());

        assert_eq!(tree.get("Hello"), Some("1".to_string()));
        assert_eq!(tree.get("hello"), Some("2".to_string()));
        assert_eq!(tree.get("HELLO"), Some("3".to_string()));
        assert_eq!(tree.get("HeLLo"), None);
    }

    #[test]
    fn test_whitespace_in_keys() {
        let mut tree = create_tree();
        tree.insert(" leading", "1".to_string());
        tree.insert("trailing ", "2".to_string());
        tree.insert(" both ", "3".to_string());
        tree.insert("mid dle", "4".to_string());
        tree.insert("\ttab", "5".to_string());
        tree.insert("newline\n", "6".to_string());

        assert_eq!(tree.get(" leading"), Some("1".to_string()));
        assert_eq!(tree.get("trailing "), Some("2".to_string()));
        assert_eq!(tree.get(" both "), Some("3".to_string()));
        assert_eq!(tree.get("mid dle"), Some("4".to_string()));
        assert_eq!(tree.get("\ttab"), Some("5".to_string()));
        assert_eq!(tree.get("newline\n"), Some("6".to_string()));
    }

    #[test]
    fn test_delete_single_key() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());
        assert_eq!(tree.get("hello"), Some("world".to_string()));

        tree.delete("hello");
        assert_eq!(tree.get("hello"), None);
    }

    #[test]
    fn test_delete_nonexistent_key() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());

        // Should not panic or affect existing keys
        tree.delete("nonexistent");
        assert_eq!(tree.get("hello"), Some("world".to_string()));
    }

    #[test]
    fn test_delete_with_prefix_preservation() {
        let mut tree = create_tree();
        tree.insert("test", "1".to_string());
        tree.insert("testing", "2".to_string());
        tree.insert("tester", "3".to_string());

        // Delete "testing" - should preserve "test" and "tester"
        tree.delete("testing");
        assert_eq!(tree.get("test"), Some("1".to_string()));
        assert_eq!(tree.get("testing"), None);
        assert_eq!(tree.get("tester"), Some("3".to_string()));
    }

    #[test]
    fn test_delete_parent_preserves_children() {
        let mut tree = create_tree();
        tree.insert("test", "parent".to_string());
        tree.insert("testing", "child1".to_string());
        tree.insert("tester", "child2".to_string());

        // Delete parent "test" - children should remain
        tree.delete("test");
        assert_eq!(tree.get("test"), None);
        assert_eq!(tree.get("testing"), Some("child1".to_string()));
        assert_eq!(tree.get("tester"), Some("child2".to_string()));
    }

    #[test]
    fn test_delete_child_preserves_parent() {
        let mut tree = create_tree();
        tree.insert("test", "parent".to_string());
        tree.insert("testing", "child".to_string());

        // Delete child "testing" - parent should remain
        tree.delete("testing");
        assert_eq!(tree.get("test"), Some("parent".to_string()));
        assert_eq!(tree.get("testing"), None);
    }

    #[test]
    fn test_delete_leaf_with_siblings() {
        let mut tree = create_tree();
        tree.insert("car", "1".to_string());
        tree.insert("card", "2".to_string());
        tree.insert("care", "3".to_string());

        // Delete "card" - siblings should remain
        tree.delete("card");
        assert_eq!(tree.get("car"), Some("1".to_string()));
        assert_eq!(tree.get("card"), None);
        assert_eq!(tree.get("care"), Some("3".to_string()));
    }

    #[test]
    fn test_delete_and_reinsert() {
        let mut tree = create_tree();
        tree.insert("hello", "world".to_string());

        tree.delete("hello");
        assert_eq!(tree.get("hello"), None);

        // Reinsert should work
        tree.insert("hello", "universe".to_string());
        assert_eq!(tree.get("hello"), Some("universe".to_string()));
    }

    #[test]
    fn test_delete_all_keys() {
        let mut tree = create_tree();
        tree.insert("one", "1".to_string());
        tree.insert("two", "2".to_string());
        tree.insert("three", "3".to_string());

        tree.delete("one");
        tree.delete("two");
        tree.delete("three");

        assert_eq!(tree.get("one"), None);
        assert_eq!(tree.get("two"), None);
        assert_eq!(tree.get("three"), None);
    }

    #[test]
    fn test_delete_empty_key() {
        let mut tree = create_tree();
        tree.insert("", "empty".to_string());
        tree.insert("nonempty", "value".to_string());

        assert_eq!(tree.get(""), Some("empty".to_string()));
        tree.delete("");
        assert_eq!(tree.get(""), None);
        assert_eq!(tree.get("nonempty"), Some("value".to_string()));
    }

    #[test]
    fn test_delete_with_node_merging() {
        let mut tree = create_tree();
        // This tests if nodes are properly merged after deletion
        tree.insert("slow", "1".to_string());
        tree.insert("slower", "2".to_string());
        tree.insert("slowly", "3".to_string());

        // Delete "slower" - the tree should potentially merge nodes if only one child remains
        tree.delete("slower");
        assert_eq!(tree.get("slow"), Some("1".to_string()));
        assert_eq!(tree.get("slower"), None);
        assert_eq!(tree.get("slowly"), Some("3".to_string()));
    }

    #[test]
    fn test_delete_unicode_keys() {
        let mut tree = create_tree();
        tree.insert("café", "coffee".to_string());
        tree.insert("naïve", "simple".to_string());
        tree.insert("日本", "Japan".to_string());

        tree.delete("naïve");
        assert_eq!(tree.get("café"), Some("coffee".to_string()));
        assert_eq!(tree.get("naïve"), None);
        assert_eq!(tree.get("日本"), Some("Japan".to_string()));
    }

    #[test]
    fn test_delete_long_key() {
        let mut tree = create_tree();
        let long_key = "a".repeat(1000);
        let another_key = "b".repeat(1000);

        tree.insert(&long_key, "long_value".to_string());
        tree.insert(&another_key, "another_value".to_string());

        tree.delete(&long_key);
        assert_eq!(tree.get(&long_key), None);
        assert_eq!(tree.get(&another_key), Some("another_value".to_string()));
    }

    #[test]
    fn test_delete_single_char_keys() {
        let mut tree = create_tree();
        tree.insert("a", "1".to_string());
        tree.insert("b", "2".to_string());
        tree.insert("c", "3".to_string());

        tree.delete("b");
        assert_eq!(tree.get("a"), Some("1".to_string()));
        assert_eq!(tree.get("b"), None);
        assert_eq!(tree.get("c"), Some("3".to_string()));
    }

    #[test]
    fn test_delete_hierarchical_paths() {
        let mut tree = create_tree();
        tree.insert("users", "all".to_string());
        tree.insert("users/john", "john_data".to_string());
        tree.insert("users/john/profile", "john_profile".to_string());
        tree.insert("users/jane", "jane_data".to_string());

        // Delete middle of hierarchy
        tree.delete("users/john");
        assert_eq!(tree.get("users"), Some("all".to_string()));
        assert_eq!(tree.get("users/john"), None);
        assert_eq!(
            tree.get("users/john/profile"),
            Some("john_profile".to_string())
        );
        assert_eq!(tree.get("users/jane"), Some("jane_data".to_string()));
    }

    #[test]
    fn test_delete_similar_keys() {
        let mut tree = create_tree();
        tree.insert("a", "1".to_string());
        tree.insert("aa", "2".to_string());
        tree.insert("aaa", "3".to_string());
        tree.insert("aaaa", "4".to_string());

        // Delete from middle
        tree.delete("aa");
        tree.delete("aaa");

        assert_eq!(tree.get("a"), Some("1".to_string()));
        assert_eq!(tree.get("aa"), None);
        assert_eq!(tree.get("aaa"), None);
        assert_eq!(tree.get("aaaa"), Some("4".to_string()));
    }

    #[test]
    fn test_delete_order_independence() {
        let mut tree1 = create_tree();
        tree1.insert("apple", "1".to_string());
        tree1.insert("application", "2".to_string());
        tree1.insert("apply", "3".to_string());

        let mut tree2 = create_tree();
        tree2.insert("apple", "1".to_string());
        tree2.insert("application", "2".to_string());
        tree2.insert("apply", "3".to_string());

        // Delete in different orders
        tree1.delete("apple");
        tree1.delete("apply");

        tree2.delete("apply");
        tree2.delete("apple");

        // Both trees should have same state
        assert_eq!(tree1.get("apple"), None);
        assert_eq!(tree1.get("application"), Some("2".to_string()));
        assert_eq!(tree1.get("apply"), None);

        assert_eq!(tree2.get("apple"), None);
        assert_eq!(tree2.get("application"), Some("2".to_string()));
        assert_eq!(tree2.get("apply"), None);
    }

    #[test]
    fn test_delete_with_special_characters() {
        let mut tree = create_tree();
        tree.insert("hello-world", "1".to_string());
        tree.insert("hello_world", "2".to_string());
        tree.insert("hello.world", "3".to_string());
        tree.insert("hello world", "4".to_string());

        tree.delete("hello_world");
        tree.delete("hello world");

        assert_eq!(tree.get("hello-world"), Some("1".to_string()));
        assert_eq!(tree.get("hello_world"), None);
        assert_eq!(tree.get("hello.world"), Some("3".to_string()));
        assert_eq!(tree.get("hello world"), None);
    }

    #[test]
    fn test_delete_stress_test() {
        let mut tree = create_tree();
        let n = 100;

        // Insert many keys
        for i in 0..n {
            let key = format!("key_{i}");
            let value = format!("value_{i}");
            tree.insert(&key, value);
        }

        // Delete even numbered keys
        for i in (0..n).step_by(2) {
            let key = format!("key_{i}");
            tree.delete(&key);
        }

        // Verify deletions and preservations
        for i in 0..n {
            let key = format!("key_{i}");
            if i % 2 == 0 {
                assert_eq!(tree.get(&key), None, "Key {i} should be deleted");
            } else {
                let expected_value = format!("value_{i}");
                assert_eq!(tree.get(&key), Some(expected_value), "Key {i} should exist");
            }
        }
    }

    #[test]
    fn test_delete_with_common_very_long_prefix() {
        let mut tree = create_tree();
        let prefix = "very_long_common_prefix_that_is_shared_by_multiple_keys_";

        tree.insert(&format!("{prefix}a"), "1".to_string());
        tree.insert(&format!("{prefix}b"), "2".to_string());
        tree.insert(&format!("{prefix}c"), "3".to_string());

        tree.delete(&format!("{prefix}b"));

        assert_eq!(tree.get(&format!("{prefix}a")), Some("1".to_string()));
        assert_eq!(tree.get(&format!("{prefix}b")), None);
        assert_eq!(tree.get(&format!("{prefix}c")), Some("3".to_string()));
    }

    #[test]
    fn test_delete_partial_key_should_not_affect_full_key() {
        let mut tree = create_tree();
        tree.insert("hello", "1".to_string());
        tree.insert("hello_world", "2".to_string());

        // Attempting to delete a partial key that doesn't exist
        tree.delete("hel");
        tree.delete("hello_");

        // Original keys should remain intact
        assert_eq!(tree.get("hello"), Some("1".to_string()));
        assert_eq!(tree.get("hello_world"), Some("2".to_string()));
    }

    #[test]
    fn test_delete_case_sensitive() {
        let mut tree = create_tree();
        tree.insert("Hello", "1".to_string());
        tree.insert("hello", "2".to_string());
        tree.insert("HELLO", "3".to_string());

        tree.delete("hello");

        assert_eq!(tree.get("Hello"), Some("1".to_string()));
        assert_eq!(tree.get("hello"), None);
        assert_eq!(tree.get("HELLO"), Some("3".to_string()));
    }

    #[test]
    fn test_delete_whitespace_keys() {
        let mut tree = create_tree();
        tree.insert(" ", "space".to_string());
        tree.insert("\t", "tab".to_string());
        tree.insert("\n", "newline".to_string());
        tree.insert("normal", "text".to_string());

        tree.delete("\t");
        tree.delete(" ");

        assert_eq!(tree.get(" "), None);
        assert_eq!(tree.get("\t"), None);
        assert_eq!(tree.get("\n"), Some("newline".to_string()));
        assert_eq!(tree.get("normal"), Some("text".to_string()));
    }
}
