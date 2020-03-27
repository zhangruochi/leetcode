## TLE 

34 / 35 test cases passed.

```python
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        def bfs(grid, i, j):
            
            
            visited = [[False] * len(grid[0]) for i in range(len(grid))]
            queue = deque([])
            level = 0
            queue.append((i,j, level))
            visited[i][j] = True
            
            while queue:
                i,j,level = queue.popleft()
                
                if i - 1 >= 0 and (not visited[i-1][j]):
                    if grid[i-1][j] == 0:
                        queue.append((i-1,j, level + 1))
                        visited[i-1][j] = True
                    else:
                        break
                
                if i + 1 < len(grid) and (not visited[i+1][j]):
                    if grid[i+1][j] == 0:  
                        queue.append((i+1,j, level+1))
                        visited[i+1][j] = True
                    else:
                        break
                            
                if j - 1 >= 0 and ((not visited[i][j-1])):
                    if grid[i][j-1] == 0:
                        queue.append((i, j-1, level+1))
                        visited[i][j-1] = True
                    else:
                        break
                    
                if j + 1 < len(grid[0]) and (not visited[i][j+1]):
                    if grid[i][j+1] == 0:
                        queue.append((i, j+1, level+1))
                        visited[i][j+1] = True
                    else:
                        break

            return level+1
        
        
        
        
        unique = set()
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res = max(res, bfs(grid, i,j))
                
                unique.add(grid[i][j])
        
        if len(unique) == 1:
            return -1
        
        return res
```         
                
                
                
    