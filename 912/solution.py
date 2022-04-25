"""
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""

import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapq.heapify(nums)
        return [heapq.heappop(nums) for i in range(n) ]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def quick_sort(nums):

            if not nums:
                return []
            
            if len(nums) == 1:
                return nums

            pivot = nums[len(nums) // 2]

            return quick_sort([_ for _ in nums if _ < pivot]) + [_ for _ in nums if _ == pivot ] + quick_sort([_ for _ in nums if _ > pivot])
        
        return quick_sort(nums)


