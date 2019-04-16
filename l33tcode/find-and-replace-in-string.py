class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        index_map = {indexes[i]: {"source": sources[i], "target": targets[i]} for i in range(len(indexes))}

        pos = 0
        result = ""

        while pos < len(S):
            if pos in index_map and S[pos:].startswith(index_map[pos]["source"]):
                    result += index_map[pos]["target"]
                    pos += len(index_map[pos]["source"])
            else:
                result += S[pos]
                pos += 1

        return result
