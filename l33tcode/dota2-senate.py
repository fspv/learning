from collections import deque


class Radiant:
    name = "Radiant"
    mark = "R"


class Dire:
    name = "Dire"
    mark = "D"


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        radiant_banned, dire_banned = 0, 0
        radiant, dire = senate.count(Radiant.mark), senate.count(Dire.mark)
        radiant_bans, dire_bans = 0, 0

        last = senate[0]

        while queue and radiant != radiant_banned and dire != dire_banned:
            left = queue.popleft()

            if left == Radiant.mark:
                if radiant_banned > 0:
                    radiant_banned -= 1
                    radiant_bans += 1
                else:
                    dire_banned += 1
                    queue.append(left)
                    last = left
            else:
                if dire_banned > 0:
                    dire_banned -= 1
                    dire_bans += 1
                else:
                    radiant_banned += 1
                    queue.append(left)
                    last = left

        return Radiant.name if last == Radiant.mark else Dire.name

    def predictPartyVictory1(self, senate: str) -> str:
        radiant_banned, dire_banned = 0, 0
        radiant_bans, dire_bans = 0, 0
        radiant, dire = senate.count(Radiant.mark), senate.count(Dire.mark)
        banned = 0

        pos = 0
        while radiant != radiant_banned and dire != dire_banned:
            pos = pos % len(senate)
            senator = senate[pos]
            if banned & 1 << pos:
                pass
            elif senator == Radiant.mark:
                if radiant_bans > 0:
                    radiant_bans -= 1
                    radiant_banned += 1
                    banned |= 1 << pos
                else:
                    dire_bans += 1
            else:
                if dire_bans > 0:
                    dire_bans -= 1
                    dire_banned += 1
                    banned |= 1 << pos
                else:
                    radiant_bans += 1
            pos += 1

        if dire == dire_banned:
            return Radiant.name

        return Dire.name
