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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        w, h = len(grid[0]), len(grid)
        
        def helper(row, col):
            nonlocal grid, w, h
            
            if row < 0 or row >= h or col < 0 or col >= w or grid[row][col] == "0":
                return 
            
            grid[row][col] = "0"
            for r, c in ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1) ):
                helper(r,c)
        
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    helper(i,j)
                    count += 1
        
        return count



def search(grid, visisted, i, j):
    if visisted[i][j] or grid[i][j] == "0":
        return 
    visisted[i][j] = True

    for new_i, new_j in [(i,j-1), (i,j+1), (i-1, j), (i+1, j)]:
        if new_i >= 0 and new_i < len(grid) and new_j >=0 and new_j < len(grid[0]):
            search(grid, visisted, new_i, new_j)
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        count = 0

        visisted = [[False] * len(grid[0]) for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visisted[i][j]:
                    continue
                if grid[i][j] == "1":
                    search(grid, visisted, i, j)
                    count += 1

        return count