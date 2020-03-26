"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        
    ## dp[k] = min{1 + dp[k-j*j]} 1 <= j * j <= k
    
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            dp[i] = min([1 + dp[i-j*j] for j in range(1, int(n**0.5)+1)])
        
        return dp[-1]

                    