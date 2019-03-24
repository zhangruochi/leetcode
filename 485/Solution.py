"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum = 0
        max_ = 0
        for num in nums:
            if num == 0:
                cum = 0
            else:
                cum += 1
            max_ = max(max_,cum)
        return max_


from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        for key,group in groupby(nums):
            if key == 1:
                count = max(count,len(list(group)))
        return count
            
        
                