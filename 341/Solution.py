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

from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = deque(nestedList)
        self.flatted = []
        self.recursive_flatted(self.nestedList)
        self.flatted = deque(self.flatted)
        
        
    
    
    def recursive_flatted(self,nestedList):
        while nestedList:
            item = nestedList.popleft()
            if item.isInteger():
                self.flatted.append(item.getInteger())
            else:
                self.recursive_flatted(deque(item.getList()))
                    
        
        
        
    
    
    

    def next(self):
        """
        :rtype: int
        """
        return self.flatted.popleft()
        
    
            
        
              
        
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.flatted else False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())