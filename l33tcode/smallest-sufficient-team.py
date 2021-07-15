from collections import defaultdict
from functools import lru_cache
from typing import Dict, List


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skill_map = {skill: index for index, skill in enumerate(req_skills)}
        all_skills = (1 << (len(req_skills))) - 1
        all_people = list(range(len(people)))

        dp: List[Dict[int, List[int]]] = [
            defaultdict(list) for _ in range(len(people) + 1)
        ]

        dp[-1][0] = []

        for person in reversed(range(len(people))):
            for init_skills in list(dp[person + 1].keys()):
                dp[person][init_skills] = min(
                    dp[person + 1][init_skills],
                    dp[person].get(init_skills, all_people),
                    key=len,
                ).copy()

                skills = init_skills

                for skill_name in people[person]:
                    skills |= 1 << skill_map[skill_name]

                dp[person][skills] = min(
                    dp[person + 1][init_skills] + [person],
                    dp[person].get(skills, all_people),
                    key=len,
                ).copy()

        return dp[0][all_skills]
