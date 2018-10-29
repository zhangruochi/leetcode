## 思路

- 在 grid 中，对每一个位置进行 DFS
- DFS搜索过的所有节点都加入 visited set，下次遇到该位置不用进行DFS搜索。
- 进行DFS搜索时，注意边界情况

```Python
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
```