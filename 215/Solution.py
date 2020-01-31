"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  
        return nums[-k]
                

from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 1:
            return -1
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for _ in range(k):
            res = heappop(nums)
        return -res


import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
        
import heapq



def quick_sort(array, k):

    mid = len(array) // 2
    left_array = [num for num in array if num > array[mid]]
    right_array = [num for num in array if num < array[mid]]
    
    left_array += [array[mid]] * (len(array) - len(left_array) - len(right_array) - 1)


    if len(left_array) == k:
        return array[mid]

    elif len(left_array) >= k+1:
        return quick_sort(left_array, k)
    else:
        return quick_sort(right_array, k - len(left_array) - 1)
    

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_sort(nums,k-1)
        
        
        