"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        ans = []
        row, col = len(matrix),len(matrix[0])
        for start in range(row * col):
            if start % 2 == 0:
                x = start if start < row else row - 1
                y = 0 if start < row else start - (row - 1)
                while x >= 0 and y < col:
                    ans.append(matrix[x][y])
                    x -= 1
                    y += 1
            else:
                x = 0 if start < col else start - (col - 1)
                y = start if start < col else col - 1
                while y >= 0 and x < row:
                    ans.append(matrix[x][y])
                    x += 1
                    y -= 1
        return ans
                