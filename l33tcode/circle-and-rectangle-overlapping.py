from math import sqrt


class Solution:
    def checkOverlap(
        self,
        radius: int,
        x_center: int,
        y_center: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def check_point_within_rect(px, py, x1, y1, x2, y2):
            return x1 <= px <= x2 and y1 <= py <= y2

        def horiz_line_intersects_circle_in(radius, x_center, y_center, b):
            tmp = radius ** 2 - (b - y_center) ** 2
            if tmp < 0:
                return set()

            return {x_center - sqrt(tmp), x_center + sqrt(tmp)}

        def vert_line_intersects_circle_in(radius, x_center, y_center, b):
            tmp = radius ** 2 - (b - x_center) ** 2
            if tmp < 0:
                return set()

            return {y_center - sqrt(tmp), y_center + sqrt(tmp)}

        xc1, yc1, xc2, yc2 = (
            x_center - radius,
            y_center - radius,
            x_center + radius,
            y_center + radius,
        )

        circle_rect_intersects_rect = [
            check_point_within_rect(xc1, yc1, x1, y1, x2, y2),
            check_point_within_rect(xc1, yc2, x1, y1, x2, y2),
            check_point_within_rect(xc2, yc1, x1, y1, x2, y2),
            check_point_within_rect(xc2, yc2, x1, y1, x2, y2),
        ]

        rect_within_circle = [
            check_point_within_rect(x1, y1, xc1, yc1, xc2, yc2),
            check_point_within_rect(x1, y2, xc1, yc1, xc2, yc2),
            check_point_within_rect(x2, y1, xc1, yc1, xc2, yc2),
            check_point_within_rect(x2, y2, xc1, yc1, xc2, yc2),
        ]

        if all(rect_within_circle):
            return True

        if all(circle_rect_intersects_rect):
            return True

        roots = horiz_line_intersects_circle_in(radius, x_center, y_center, y1)
        for root in roots:
            if x1 <= root <= x2:
                return True

        roots = horiz_line_intersects_circle_in(radius, x_center, y_center, y2)
        for root in roots:
            if x1 <= root <= x2:
                return True

        roots = vert_line_intersects_circle_in(radius, x_center, y_center, x1)
        for root in roots:
            if y1 <= root <= y2:
                return True

        roots = vert_line_intersects_circle_in(radius, x_center, y_center, x2)
        for root in roots:
            if y1 <= root <= y2:
                return True

        return False


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.checkOverlap(
            radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1
        )

    def test_case2(self):
        assert self.sol.checkOverlap(
            radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1
        )

    def test_case3(self):
        assert self.sol.checkOverlap(
            radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3
        )

    def test_case4(self):
        assert not self.sol.checkOverlap(
            radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1
        )

    def test_case5(self):
        assert self.sol.checkOverlap(5, 8, 8, 9, 5, 12, 8)

    def test_case6(self):
        assert self.sol.checkOverlap(18, 11, 19, 7, 12, 10, 20,)

    def test_case7(self):
        assert self.sol.checkOverlap(11, 13, 1, 9, 8, 18, 18,)
