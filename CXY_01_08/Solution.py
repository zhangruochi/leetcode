"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

 

示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zero-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])

        row0_flag = False
        for j in range(n):
            if matrix[0][j] == 0:
                row0_flag = True
                break

        col0_flag = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0_flag = True
                break
                
        # save informatoin row_1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for row in range(1,m):
            if matrix[row][0] == 0:
                for col in range(1,n):
                    matrix[row][col] = 0


        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1,m):
                    matrix[row][col] = 0


        if row0_flag:
            for col in range(n):
                matrix[0][col] = 0

        if col0_flag:
            for row in range(m):
                matrix[row][0] = 0
        
        return matrix
