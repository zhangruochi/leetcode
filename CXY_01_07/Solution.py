class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #  matrix[col][n-row-1] =  matrix[row][col] 

        # 水平翻转 matrix[n-row-1][col]   = matrix[row][col]
        # 对角线翻转  matrix[col][n-row-1]  =   matrix[row][col]


        N = len(matrix)

        for row in range(N // 2):
            for  col in range(N):
                matrix[N-row-1][col], matrix[row][col] = matrix[row][col], matrix[N-row-1][col]

        
        for row in range(N):
            for col in range(row + 1):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

        
        return matrix
