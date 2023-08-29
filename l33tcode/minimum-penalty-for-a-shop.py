class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")  # When we're always closed

        min_closing_time = 0
        min_penalty = penalty

        for closing_time in range(len(customers)):
            if customers[closing_time] == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty < min_penalty:
                # `closing_time` 0 means we actually are still open and will
                # only close at the next timestamp
                min_closing_time = closing_time + 1
                min_penalty = penalty

        return min_closing_time
