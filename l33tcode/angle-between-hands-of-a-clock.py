class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        def hour_to_angle(hour: int, minute: int) -> int:
            if hour == 12:
                hour = 0
            return hour * 360 / 12 + minute * 360 / (12 * 60)

        def minute_to_angle(minute: int) -> int:
            return minute * 360 / 60

        angle = abs(hour_to_angle(hour, minutes) - minute_to_angle(minutes))

        return min(360 - angle, angle)
