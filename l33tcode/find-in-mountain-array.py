from __future__ import annotations

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:
    def get(self, index: int) -> int:
        raise NotImplementedError()

    def length(self) -> int:
        raise NotImplementedError()


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        left, right = 0, mountain_arr.length() - 1
        # Discard invalid parts as we search and track valid region here
        next_left, next_right = left, right

        # Search uphill (left) part
        while left < right:
            mid = left + (right - left) // 2

            this_val = mountain_arr.get(mid)
            next_val = mountain_arr.get(mid + 1)

            # below on the left (uphill) slope
            if this_val < next_val and this_val < target:
                left = mid + 1
            else:
                right = mid

            # discard uphill or above on the right (downhill) slope
            if this_val < next_val or this_val > target:
                next_left = max(next_left, mid + 1)
            else:
                next_right = min(next_right, mid)

        # Check if found
        if mountain_arr.get(left) == target:
            return left

        # Search the rest (not discarded earlier)
        left, right = next_left, next_right

        while left < right:
            mid = left + (right - left) // 2

            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid

        # Check if found
        if mountain_arr.get(left) == target:
            return left

        return -1

    def findInMountainArray2(self, target: int, mountain_arr: "MountainArray") -> int:
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
