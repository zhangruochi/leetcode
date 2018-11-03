## 思路


- 采用BFS的思路，对图中的每个节点进行搜索。
- 如果该结点为"1",且该结点没有被访问过，则BFS该结点，并且把所有能访问到的结点设置为已访问
- 由上面的思路可以避免重复访问已访问的岛屿

```Python
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
```