"""
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A. 

As the answer may be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000
"""


## TLE

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        res = 0
        
        
        def get_width(sub):
            return max(sub) - min(sub)
        
        def recursive(A, seq, pos):
            nonlocal res
            
            for i in range(pos, len(A)):
                seq.append(A[i])
                res += get_width(seq)
                recursive(A, seq, i+1)
                seq.pop()
       
        recursive(A, [], 0)
        
        return res % (10**9 + 7)
    

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        """
        1. key obervation: sorting will not change the answer
        2. A[i]'s contribution: A[i] * 2^i - A[i] * 2^(n-i-1)
        """
        res = 0
        init_prod = 2 ** len(A)
        A.sort()
        
        for i in range(len(A)):
            
            if  i == 0:
                cum_prod_upper = 1
                cum_prod_lower = (init_prod // cum_prod_upper) >> 1
            else:
                cum_prod_upper *= 2
                cum_prod_lower >>= 1

            res += (A[i] * cum_prod_upper - A[i]*cum_prod_lower)
        
        return res % (10**9 + 7)

             
        
        

             
        
        