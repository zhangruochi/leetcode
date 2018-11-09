"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""



class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if not A:
            return 0
        
        left,right = 1,len(A)-2
        dp1,dp2 = [0],[0]
        
            
        while left < len(A):
            ## 求当前元素之前有多少个元素小于这个元素
            if A[left] > A[left-1]:
                dp1.append(dp1[-1]+1)
            else:
                dp1.append(0)
                
            ## 求当前元素之前有多少个元素大于这个元素
            if A[right] > A[right+1]:
                dp2.append(dp2[-1]+1)
            else:
                dp2.append(0)
            
            left += 1
            right -= 1
        
        dp2.reverse()
        
        max_ = 0
        for i in range(len(dp1)):
            if dp1[i] == 0 or dp2[i] == 0:
                continue
            else:
                max_ = max(max_,dp1[i]+dp2[i]+1)
        
        
        return max_
    