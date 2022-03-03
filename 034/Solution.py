"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109<= nums[i]<= 109
nums is a non-decreasing array.
-109<= target<= 109


"""

def binary_search_left(nums, target, left, right):
    if left > right:
        return -1
    
    mid  = (left + right) // 2

    if nums[mid] == target:
        if mid == 0 or nums[mid-1] < target:
            return mid
        else:
            return binary_search_left(nums, target, left, mid-1)
    elif nums[mid] > target:
        return binary_search_left(nums, target, left, mid-1)
    elif nums[mid] < target:
        return binary_search_left(nums, target, mid+1, right)
        

def binary_search_right(nums, target, left, right):
    if left > right:
        return -1
    
    mid  = (left + right) // 2

    if nums[mid] == target:
        if mid == len(nums)-1 or nums[mid+1] > target:
            return mid
        else:
            return binary_search_right(nums, target, mid+1, right)
    elif nums[mid] > target:
        return binary_search_right(nums, target, left, mid-1)
    elif nums[mid] < target:
        return binary_search_right(nums, target, mid+1, right)
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1,-1]

        return [binary_search_left(nums, target, 0, len(nums)-1), binary_search_right(nums, target, 0, len(nums)-1)]

