#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or 
equal to m + n) to hold additional elements from nums2. The number 
of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):
    def merge_me(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cur_num1 = 0
        cur_num2 = 0

        while True:
            if cur_num2 == n:
                break

            elif cur_num1 == m:
                nums1.append(nums2[cur_num2])
                cur_num2 += 1
                continue    
            
            elif nums1[cur_num1] < nums2[cur_num2]:
                cur_num1 += 1
                continue

            elif nums1[cur_num1] >= nums2[cur_num2]:
                nums1.insert(cur_num1, nums2[cur_num2])
                cur_num1 += 1
                cur_num2 += 1
                m += 1         

        print(nums1) 

        def merge(self, nums1, m, nums2, n):
            while m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[m+n-1] = nums1[m-1]
                    m -= 1
                else:
                    nums1[m+n-1] = nums2[n-1]
                    n -= 1
            if n > 0:
                nums1[:n] = nums2[:n]



if __name__ == '__main__':
    solution = Solution()
    solution.merge([0], 1, [1],1 )
