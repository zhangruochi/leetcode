"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = [[0] * len(grid[0]) for i in range(len(grid))]

        sum_ = 0
        for i in range(len(grid[0])):
            sum_ += grid[0][i]
            dp[0][i] = sum_
        
        sum_ = 0
        for j in range(len(grid)):
            sum_ += grid[j][0]
            dp[j][0] = sum_
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
