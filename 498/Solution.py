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
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]: return []
        
        i = j = 0
        direction = 1
        M,N = len(matrix)-1,len(matrix[0])-1
        res = []
        count = 0
        while count < (M+1)*(N+1):
            res.append(matrix[i][j])
            count += 1
            if i == 0 and direction == 1:
                direction = 0
                if j == N:
                    i += 1
                else:
                    j += 1
                continue
                
            if j == 0 and direction == 0:
                direction = 1
                if i == M:
                    j += 1
                else:
                     i+= 1
                continue
                
            if i == M and direction == 0:
                direction = 1
                j += 1
                continue
                
            if j == N and direction == 1:
                direction = 0
                i += 1
                continue
                
            if direction == 0:
                i += 1
                j -= 1
            else:
                i -= 1
                j += 1
        return res
                


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
                