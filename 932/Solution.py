"""
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]
 

Note:

1 <= N <= 1000
"""


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1:
            return [N]
        
        if N == 2:
            return [1,2]
        
        left = self.beautifulArray((N+1)//2)
        right = self.beautifulArray(N//2)
        
        return [num*2-1 for num in left] + [num*2 for num in right]
    


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        
        memory = dict()
        def helper(N):
            if N in memory:
                return memory[N]
            if N == 1:
                return [N]

            if N == 2:
                return [1,2]

            left = self.beautifulArray((N+1)//2)
            right = self.beautifulArray(N//2)

            res = [num*2-1 for num in left] + [num*2 for num in right]
            
            memory[N] = res
            
            return res
        
        return helper(N)
        