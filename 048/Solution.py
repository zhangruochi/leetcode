"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])

        res = [[-1]*m for i in range(n)]

        # 对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置

        for i in range(n):
            for j in range(m):
                res[j][n-i-1] = matrix[i][j]

        for i in range(n):
            for j in range(m):
                matrix[i][j] = res[i][j]

        return matrix
        


