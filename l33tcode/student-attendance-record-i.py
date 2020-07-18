class Solution:
    def checkRecord(self, s: str) -> bool:
        def check_absent(count):
            return count <= 1

        def check_late(count):
            return count <= 2

        absent_count, late_count = 0, 0

        for char in s:
            if char == "A":  # absent
                absent_count += 1

            if char == "L":  # late
                late_count += 1
            else:
                late_count = 0

            if not check_absent(absent_count):
                return False

            if not check_late(late_count):
                return False

        return True
