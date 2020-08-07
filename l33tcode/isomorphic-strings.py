class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mutation_fwd = {}
        mutation_back = {}

        for pos in range(len(s)):
            mutation_fwd.setdefault(s[pos], t[pos])
            mutation_back.setdefault(t[pos], s[pos])
            if mutation_fwd[s[pos]] != t[pos]:
                return False
            if mutation_back[t[pos]] != s[pos]:
                return False

        return True
