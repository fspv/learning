# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        def find_apex():
            left, right = 1, mountain_arr.length() - 2

            def condition(pos: int) -> bool:
                return mountain_arr.get(pos) < mountain_arr.get(pos + 1)

            while left < right:
                middle = left + (right - left) // 2

                if condition(middle):
                    left = middle + 1
                else:
                    right = middle

            return left

        def bisect(left: int, right: int, target: int, forward: bool) -> int:
            def condition(pos: int, reverse: bool) -> bool:
                if forward:
                    return mountain_arr.get(pos) < target
                else:
                    return mountain_arr.get(pos) > target

            while left < right:
                middle = left + (right - left) // 2

                if condition(middle, forward):
                    left = middle + 1
                else:
                    right = middle

            return left

        apex = find_apex()

        left_result = bisect(0, apex, target, True)

        if mountain_arr.get(left_result) == target:
            return left_result

        right_result = bisect(apex + 1, mountain_arr.length() - 1, target, False)

        if mountain_arr.get(right_result) == target:
            return right_result

        return -1
