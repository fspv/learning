from functools import lru_cache
from typing import List, Set


def sieve(limit: int = 10001) -> List[int]:
    primes: Set[int] = set(range(2, limit))

    for num in range(2, limit):
        if num in primes:
            total = num
            while total + num < limit:
                total += num
                primes.discard(total)

    return list(sorted(primes))


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        primes = sieve()

        result: List[int] = []

        @lru_cache(None)
        def backtrack(items: int, buckets: int) -> int:
            if buckets == 1:
                return 1

            if items == 0:
                return 1

            if items == 1:
                return buckets

            count = 0

            for new_items in range(items + 1):
                count += backtrack(new_items, buckets - 1)

            return count

        for n, k in queries:
            # Handle the situation number itself is prime
            count = 1 if k not in primes else n

            for prime in primes:
                if prime >= k // 2 + 1:
                    break

                if k % prime == 0:
                    repeats = 0
                    left = k
                    while left % prime == 0:
                        repeats += 1
                        left //= prime

                    count *= backtrack(repeats, n)

            result.append(count % (10**9 + 7))

        return result

    def waysToFillArrayBruteForce(self, queries: List[List[int]]) -> List[int]:
        primes = sieve()
        primes_set = set(primes)

        @lru_cache(None)
        def get_prime_divisors(number: int, prime: int) -> Set[int]:
            divisors: Set[int] = set()

            for divisor in range(prime, number // 2 + 1, prime):
                if number % divisor == 0:
                    divisors.add(divisor)

                    if divisor != number // divisor:
                        divisors.add(number // divisor)

            return divisors

        @lru_cache(None)
        def get_divisors(number: int) -> Set[int]:
            if number == 1:
                return {1}

            divisors: Set[int] = {1, number}

            for prime in primes:
                if prime > number:
                    break

                divisors |= get_prime_divisors(number, prime)

            return divisors

        @lru_cache(None)
        def backtrack(number: int, left: int) -> int:
            if left == 1:
                return 1

            if number in primes_set:
                return left

            count = 0
            divisors = get_divisors(number)

            for divisor in divisors:
                count += backtrack(number // divisor, left - 1)

            return count % (10**9 + 7)

        return [backtrack(k, n) for n, k in queries]
