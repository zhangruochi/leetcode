# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def binarySearch(self,low, high):
        if high < low:
            return -1
        mid = low + (( high - low ) >> 1)
        if not isBadVersion(mid):
            return self.binarySearch(mid+1,high)
        else:
            if mid == 0 or not isBadVersion(mid-1):
                return mid
            else:
                return self.binarySearch(low,mid-1)
      
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1,n)