class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = (1 + len(nums)) * len(nums) // 2
        for num in nums:
            sum_ -= num
        
        return sum_


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(1,len(nums)+1):
            x = x^i^nums[i-1]
        return x