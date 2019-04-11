class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if not s or not dict:
            return s

        dict_set = set(dict)
        dict_max_len = max([len(item) for item in dict])
        intervals = []

        for left_pos in range(len(s)):
            for right_pos in range(left_pos, min(len(s), left_pos + dict_max_len)):
                if s[left_pos:right_pos + 1] in dict_set:
                    intervals.append((left_pos, right_pos))

        stack = []
        for interval in intervals:
            if stack:
                prev_left, prev_right = stack[-1]
                left, right = interval

                if left <= prev_right + 1:
                    stack.pop()
                    stack.append((prev_left, max(right, prev_right)))
                else:
                    stack.append(interval)
            else:
                stack.append(interval)


        result = ""
        prev_right = 0
        for pos in range(len(stack)):
            left, right = stack[pos]
            result += s[prev_right:left]
            result += "<b>"
            result += s[left:right + 1]
            result += "</b>"
            prev_right = right + 1

        result += s[prev_right:]

        return result
