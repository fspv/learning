#[allow(dead_code)]
struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

use std::{cmp::Reverse, collections::BinaryHeap};

impl Ord for ListNode {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.val.cmp(&other.val)
    }
}

impl PartialOrd for ListNode {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    #[allow(dead_code)]
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut heap = BinaryHeap::new();

        for node in lists.into_iter().flatten() {
            heap.push(Reverse(node));
        }

        if heap.is_empty() {
            return None;
        }

        let mut dummy = ListNode::new(-1);

        let mut current = &mut dummy;

        while let Some(Reverse(mut node)) = heap.pop() {
            if let Some(next_node) = node.next.take() {
                heap.push(Reverse(next_node));
            }

            current.next = Some(node);
            current = current.next.as_mut().unwrap();
        }

        dummy.next
    }
}
