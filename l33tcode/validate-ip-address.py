import string


class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validate_ipv6(ip: str) -> bool:
            groups = ip.split(":")

            if len(groups) != 8:
                return False

            for group in groups:
                if len(group) < 1:
                    return False

                for char in group:
                    if char.lower() not in string.hexdigits:
                        return False

                if len(group) > 4:
                    return False

            return True

        def validate_ipv4(ip: str) -> bool:
            octets = ip.split(".")

            if len(octets) != 4:
                return False

            for octet in octets:
                if len(octet) < 1:
                    return False

                if octet.startswith("0") and len(octet) > 1:
                    return False

                for char in octet:
                    if char not in string.digits:
                        return False

                if int(octet) > 255:
                    return False

            return True

        if validate_ipv4(IP):
            return "IPv4"
        elif validate_ipv6(IP):
            return "IPv6"

        return "Neither"
