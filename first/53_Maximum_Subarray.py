#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray_me(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        subarray = [nums[nums.index(max_sum)]]

        for index,num in enumerate(nums):
            sum = 0
            if num < 0:
                continue
            for stop,num in enumerate(nums[index:]):
                if num > 0:
                    sum += num
                    if sum > max_sum:
                        max_sum = sum
                        subarray = nums[index:index + stop + 1]
                else:
                    sum += num

        return max_sum,subarray

    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))               
                    

