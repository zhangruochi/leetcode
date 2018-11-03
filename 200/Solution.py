"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0]*len(grid[0]) for i in range(len(grid))]

        def bfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or visited[i][j] == 1:
                return
            
            visited[i][j] = 1
            
            bfs(grid,i-1,j)
            bfs(grid,i+1,j)
            bfs(grid,i,j-1)
            bfs(grid,i,j+1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs(grid,i,j)
                    count += 1
        
        return count