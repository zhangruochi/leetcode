'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]        

    def singleNumber2(self,nums):
        return reduce(operator.xor,nums)
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))
    print(solution.singleNumber2([4,1,2,1,2]))








