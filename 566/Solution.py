"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(mat) * len(mat[0]) != r * c:
            return mat

        res = [[-1] * c for _ in range(r)]
        all_v = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]

        index = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = all_v[index]
                index += 1

        return res

