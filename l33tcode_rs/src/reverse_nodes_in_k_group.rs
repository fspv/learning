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
    #[allow(dead_code)]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut head = head;

        // Try to traverse forward k steps
        let mut node = &mut head;

        for _ in 0..k {
            match node {
                Some(n) => {
                    node = &mut n.next;
                }
                _ => return head,
            }
        }

        // Get the rest of the list reversed
        let new_head = Self::reverse_k_group(node.take(), k);

        // Now reverse this part of the list and connect it to the head returned from the rest of
        // the list
        let mut node = head;
        let mut prev_node = new_head;

        for _ in 0..k {
            let mut current = node.unwrap();
            let next_node = current.next;
            current.next = prev_node;
            prev_node = Some(current);
            node = next_node;
        }

        prev_node
    }
}
