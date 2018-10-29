"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution:
    
    def get_max(self,land,grid,visited):
        island = 0
        stack = [land]
        visited.add(land)
        while stack:
            i,j = stack.pop()
            island += 1
            if i-1 >= 0:
                next_land = (i-1,j)
                if next_land not in visited and grid[i-1][j] == 1:
                    visited.add(next_land)
                    stack.append(next_land)
            if i+1 <= len(grid)-1:
                next_land = (i+1,j)
                if next_land not in visited and grid[i+1][j] == 1:
                    visited.add(next_land)
                    stack.append(next_land)
            if j-1 >= 0:
                next_land = (i,j-1)
                if next_land not in visited and grid[i][j-1] == 1:
                    visited.add(next_land)
                    stack.append(next_land)    
            if j+1 <= len(grid[0])-1:
                next_land = (i,j+1)
                if next_land not in visited and grid[i][j+1] == 1:
                    visited.add(next_land)
                    stack.append(next_land)
        
        return island
         
        
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    island = self.get_max((i,j),grid,visited)
                    if island > max_island:
                        max_island = island
                    
        return max_island
        