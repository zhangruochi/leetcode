"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return board

        cache = [[False] * len(board[0]) for _ in range(len(board))]


        def visit(board, i, j):
            nonlocal cache

            board[i][j] = "Y"
            cache[i][j] = True

            for next_i, next_j in [(i-1, j), (i+1,j), (i, j-1), (i, j+1)]:
                if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) and board[next_i][next_j] == "O" and not cache[next_i][next_j]:
                    visit(board, next_i, next_j)

        for j in range(len(board[0])):
            if board[0][j] == "O":
                visit(board, 0, j)
            
            if board[len(board)-1][j] == "O":
                visit(board, len(board)-1, j)
        
        for i in range(len(board)):
            if board[i][0] == "O":
                visit(board, i, 0)

            if board[i][len(board[0])-1] == "O":
                visit(board, i, len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        return board

        
            