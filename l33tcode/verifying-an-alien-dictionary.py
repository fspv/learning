class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {k: v for v, k in enumerate(order)}
        max_word_len = len(max(words, key=lambda x: len(x)))

        for pos in range(max_word_len):
            prev = order_dict[words[0][pos]] if pos < len(words[0]) else -1
            for pos_w in range(len(words)):
                if words[pos_w] is None:
                    continue

                current = order_dict[words[pos_w][pos]] if pos < len(words[pos_w]) else -1 
                if current < prev:
                    return False
                elif current > prev:
                    words[pos_w] = None
                prev = current

        return True
