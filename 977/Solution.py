"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A: return []
        for i in range(len(A)):
            if A[i] >=0:
                break
        res = []
        j = i-1
        
        while j > -1 and i < len(A):
            if A[i] < -A[j]:
                res.append(A[i]**2)
                i += 1
            else:
                res.append(A[j]**2)
                j -= 1
        if A[i:]:
            res += [item**2 for item in A[i:]]
        else:
            res += [item**2 for item in A[:j+1][::-1]]
        
        return res
                
            
        