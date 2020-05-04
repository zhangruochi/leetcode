"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []

        res = []

        directions = ((0,1),(1,0),(0,-1),(-1,0))
        upper_n,upper_m = len(matrix), len(matrix[0])
        low_n,low_m, n, m = 0, 0, 0, 0

        index = 0
        while True:

            d = directions[index % 4]
       
            while low_n <= n < upper_n and low_m <= m < upper_m:
                res.append(matrix[n][m])
                n += d[0]
                m += d[1]

            if m >= upper_m:
                m -= 1

                low_n += 1
                n += 1
            
            if n >= upper_n:
                n -= 1

                upper_m -= 1
                m -= 1

            if m < low_m:
                m += 1

                upper_n -= 1
                n -= 1
            
            if n < low_n:
                n += 1
                
                low_m += 1
                m += 1
            
            # print([n,m, low_n, upper_n, low_m, upper_m])
            index  += 1

            if index > len(matrix[0]) * len(matrix):
                break

        return res