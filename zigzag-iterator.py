class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.pos1 = 0
        self.pos2 = 0
        self.switch = True


    def next(self):
        """
        :rtype: int
        """
        self.switch = not self.switch

        if self.switch:
            if self.pos2 < len(self.v2):
                self.pos2 += 1
                return self.v2[self.pos2 - 1]
            elif self.pos1 < len(self.v1):
                self.pos1 += 1
                return self.v1[self.pos1 - 1]
        else:
            if self.pos1 < len(self.v1):
                self.pos1 += 1
                return self.v1[self.pos1 - 1]
            elif self.pos2 < len(self.v2):
                self.pos2 += 1
                return self.v2[self.pos2 - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos2 < len(self.v2) or self.pos1 < len(self.v1)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
