"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0,len(nums)-1,3):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]   

    def singleNumber2(self,nums):
        a = 0; b = 0
        for i in range(len(nums)):
            b = b^nums[i] & ~a
            a = a^nums[i] & ~b

        return b             

if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([0,1,0,1,0,1,99])) 
    print(solution.singleNumber2([0,1,0,1,0,1,99]))       