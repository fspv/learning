# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.container = nestedList
        self.stack = [-1]
        self.has_next_res = False
        self.has_next_counter = 0

    def _elem_exists_in_stack(self):
        cont = self.container

        for index in self.stack:
            cont_list = cont if isinstance(cont, list) else cont.getList()
            if index >= len(cont_list):
                return False
            else:
                cont = cont_list[index]

        return True

    def _get_elem_from_stack(self):
        cont = self.container

        for index in self.stack:
            cont_list = cont if isinstance(cont, list) else cont.getList()
            cont = cont_list[index]

        return cont

    def next(self):
        """
        :rtype: int
        """
        self.has_next_counter = 0

        return self._get_elem_from_stack().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.has_next_counter > 0:
            return self.has_next_res

        self.has_next_counter += 1

        while self.stack:
            self.stack[-1] += 1

            if self._elem_exists_in_stack():
                elem = self._get_elem_from_stack()
                if elem.isInteger():
                    self.has_next_res = True
                    return self.has_next_res
                else:
                    self.stack.append(-1)
            else:
                self.stack.pop()

        self.has_next_res = False
        return self.has_next_res

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
