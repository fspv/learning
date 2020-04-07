class Solution:
    def countElements(self, arr: List[int]) -> int:
        all_elements = set(arr)
        return len([None for a in arr if (a + 1) in all_elements])
