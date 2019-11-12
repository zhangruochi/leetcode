import copy
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        W = len(grid[0])
        H = len(grid)
        
        visited = [ [False] * W for i in range(H) ]
        res = copy.deepcopy(grid)
        init = grid[r0][c0]
        
        
        def color_or_not(r,c):
            nonlocal init
            if r-1 >= 0 and grid[r-1][c] == init and c-1 >= 0 and grid[r][c-1] == init and r+1 < H and grid[r+1][c] == init and c+1 < W and grid[r][c+1] == init:
                return False
            else:
                return True
        
        
        def helper(visited,r,c):
            nonlocal res

            for new_r,new_c in ((r,c+1),(r,c-1),(r+1,c),(r-1,c)):
                if  H > new_r >=0 and W > new_c >= 0 and (not visited[new_r][new_c]) and grid[new_r][new_c] == init:
                    if color_or_not(new_r,new_c):
                        res[new_r][new_c] = color
                    visited[new_r][new_c] = True
                    helper(visited,new_r,new_c)
        
        visited[r0][c0] = True
        if color_or_not(r0,c0):
            res[r0][c0] = color
        helper(visited,r0,c0)
    
        return res
            
                