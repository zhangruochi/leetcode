"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""


from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == 0 or len(q) == m*n:
            return -1

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                        q.append((new_i,new_j))
                        grid[new_i][new_j] = 1
            level += 1
                        
        return level-1