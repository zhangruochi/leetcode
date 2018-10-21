"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution:
    def insert_sort(self,lists,m,n):
        for i in range(m,m+n):
            tmp = lists[i]
            j = i-1
            while j >= 0:
                if tmp < lists[j]:
                    lists[j+1] = lists[j]
                    j -= 1
                else:
                    break
            lists[j+1] = tmp
        
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:m+n] = nums2
        if not m:
            return
        self.insert_sort(nums1,m,n)


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        p1,p2,p_merge = m - 1, n - 1, m + n - 1

        while p1>= 0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1        

        if p2 >= 0:
            nums1[:p_merge+1] = nums2[:p2+1]  


        










