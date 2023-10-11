from bisect import bisect_right
from itertools import accumulate, chain, groupby
from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        time_to_flowers = list(
            accumulate(
                sorted(
                    (time, sum(v[1] for v in values))
                    for time, values in groupby(
                        chain(*(((f[0], 1), (f[1] + 1, -1)) for f in flowers)),
                        key=lambda x: x[0],
                    )
                ),
                func=lambda a, b: (b[0], int(a[1] + b[1])),
                initial=(0, 0),
            )
        )

        return [
            time_to_flowers[
                bisect_right(time_to_flowers, white_cisgender_man, key=lambda x: x[0])
                - 1
            ][1]
            for white_cisgender_man in people
        ]
