"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float("inf")
        nums.sort()
        res = None
        for i in range(len(nums)-2):
            fix = nums[i]
            left = i+1; right = len(nums)-1
            while left < right:
                tmp_sum = fix + nums[left] + nums[right]
                if abs(tmp_sum - target) < min_diff :
                    min_diff = abs(tmp_sum - target)
                    res = tmp_sum
                if tmp_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return res
                    

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) <= 2:
            return -1

        nums.sort()
        min_diff = float("inf")
        res_index = None
        
        for i in range(len(nums)-2):
            f = nums[i]
            j=i+1
            k = len(nums)-1
            while j<k:
                diff = abs(nums[k] + nums[j] + f - target)
                if diff < min_diff:
                    min_diff = diff
                    res_index = [i,j,k]
                    print(res_index)

                if nums[j] + nums[k] < target - f:
                    j += 1
                else:
                    k -= 1
                    
        return sum([nums[_] for _ in res_index])
                    
                    
                    