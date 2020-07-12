import string


class Solution:
    def reformatDate(self, date: str) -> str:
        def day_str_to_num(day_str: str) -> str:
            day = day_str.rstrip(string.ascii_lowercase)
            if len(day) == 1:
                return "0" + day

            return day

        def month_str_to_num(month: str) -> str:
            months = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12",
            }

            return months[month]

        def year_str_to_num(year: str) -> str:
            return year

        day, month, year = date.split()

        return (
            f"{year_str_to_num(year)}-{month_str_to_num(month)}-{day_str_to_num(day)}"
        )
