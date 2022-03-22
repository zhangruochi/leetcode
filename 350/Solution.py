"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table_num1 = Counter(nums1)
        table_num2 = Counter(nums2)
        
        result = []
        for key,value in table_num1.items():
            if key in table_num2:
                result += [key] * min(value,table_num2[key])
        return result
            

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        if not nums1 or not nums2:
            return []

        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)

        int_keys = set(nums1_dict.keys()).intersection(set(nums2_dict.keys()))

        res = []
        for _ in int_keys:
            res.extend( [_] * min(nums1_dict[_], nums2_dict[_]))

        return res