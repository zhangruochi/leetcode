"""
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
说明：r 和 c 的值均不超过 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import lru_cache

class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = []
        path = [[0,0]]

        @lru_cache(typed=False, maxsize=12800000)
        def help(r, c):
            nonlocal res, path

            if  r >= m or c >= n or obstacleGrid[r][c] == 1 or res:
                return

            if (r,c) == (m-1,n-1):
                res = path[:]
                return
            
            for new_r, new_c in ((r+1,c),(r, c+1)): 
                if not res:
                    path.append([new_r,new_c])               
                    help(new_r, new_c) 
                    path.pop()

        help(0, 0)

        return res

