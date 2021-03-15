import random
import string

from typing import List, Dict
from functools import lru_cache


class Codec:
    url_length = 8
    url_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    url_max_value = len(url_symbols) ** 8

    @lru_cache(None)
    def map(self) -> Dict[str, str]:
        return {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:  # This potentially give infinite complexity
            number = random.randint(0, self.url_max_value)

            url_letters: List[str] = []

            for _ in range(self.url_length):
                url_letters.append(self.url_symbols[number % len(self.url_symbols)])
                number //= len(self.url_symbols)

            url = "".join(url_letters)

            if url not in self.map():
                self.map()[url] = longUrl
                return url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map()[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
