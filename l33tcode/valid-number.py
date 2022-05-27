class Solution:
    def isNumber(self, string: str) -> bool:
        def validate_integer(text: str) -> bool:
            text = text.lstrip("+-")

            if not text:
                return False

            if set(text) - set("0123456789"):
                return False

            return True

        def validate_float(text: str) -> bool:
            text = text.lstrip("+-")

            if not text:
                return False

            if set(text) - set("0123456789."):
                return False

            if text.count(".") > 1:
                return False

            if text.count(".") == 0:
                return validate_integer(text)

            left, right = text.split(".")

            if not left and not right:
                return False

            if not right:
                return validate_integer(left)

            if not left:
                return validate_integer(right)

            return validate_integer(left) and validate_integer(right)

        string = string.lower()

        if set(string) - set("0123456789.+-e"):
            return False

        if string.count("e") > 1:
            return False

        if "e" in string:
            number, exponent = string.split("e")
            if not validate_float(number):
                return False
            if not validate_integer(exponent):
                return False
        else:
            number = string
            if not validate_float(number):
                return False

        return True
