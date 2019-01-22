class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        elem_hash_map = {}
        for elem in A:
            if elem in elem_hash_map:
                return elem
            else:
                elem_hash_map[elem] = None

# No testing because it is quite obvious
