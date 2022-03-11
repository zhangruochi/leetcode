"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or (not grid[0]):
            return -1

        if grid[0][0] != 0:
            return -1
    
        queue = deque()
        start = (0,0,1)

        visied = [[False] * len(grid[0]) for _ in range(len(grid))]
        queue.append(start)
        visied[0][0] = True

        end_i, end_j = len(grid)-1, len(grid[0])-1

        while queue:
            i,j, level = queue.popleft()

            if (i,j) == (end_i, end_j):
                return level
            
            for i_step, j_step in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
                next_i, next_j = i + i_step, j + j_step

                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid) and (not visied[next_i][next_j]) and grid[next_i][next_j] == 0:
                    queue.append((next_i, next_j, level + 1))
                    visied[next_i][next_j] = True
            

        return -1
