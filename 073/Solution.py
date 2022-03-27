"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        visited_rows = set()
        visited_cols = set()

        m,n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:                    
                    visited_cols.add(c)
                    visited_rows.add(r)

        for i in visited_cols:
            for r in range(m):
                matrix[r][i] = 0

        for j in visited_rows:
            for c in range(n):
                matrix[j][c] = 0
        