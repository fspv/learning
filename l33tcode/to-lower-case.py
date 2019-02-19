class Solution:
    def toLowerCase(self, string: 'str') -> 'str':
        out_str = ""

        for symbol in string:
            symbol_number = ord(symbol)
            if symbol_number > 64 and symbol_number < 91:
                out_str += chr(symbol_number + 32)
            else:
                out_str += symbol

        return out_str
