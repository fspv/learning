from typing import List, Dict


class IntTrieNode:
    def __init__(self) -> None:
        self.children: Dict[int, IntTrieNode] = {}


def trie_add(root: IntTrieNode, num: int) -> None:
    node = root

    for shift in reversed(range(32)):
        cur_bit = (num >> shift) & 1
        node.children.setdefault(cur_bit, IntTrieNode())
        node = node.children[cur_bit]


def trie_largest_xor(root: IntTrieNode, num: int) -> int:
    node = root

    result = 0

    for shift in reversed(range(32)):
        inv_bit = ~(num >> shift) & 1
        cur_bit = (num >> shift) & 1

        result <<= 1

        if inv_bit in node.children:
            result |= 1
            node = node.children[inv_bit]
        else:
            node = node.children[cur_bit]

    return result


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = IntTrieNode()

        for num in nums:
            trie_add(root, num)

        result = 0

        for num in nums:
            result = max(result, trie_largest_xor(root, num))

        return result

    def findMaximumXOR1(self, nums: List[int]) -> int:
        result = 0

        for mask_len in reversed(range(32)):
            prefixes = {num >> mask_len for num in nums}

            result <<= 1

            for prefix in prefixes:
                if (result | 1) ^ prefix in prefixes:
                    result |= 1

        return result
