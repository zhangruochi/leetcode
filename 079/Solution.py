"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if not board: return False
        
        
        def rec_dfs(i,j,word):
            if len(word) == 1 and board[i][j] == word:
                return True
            
            if board[i][j] != word[0]:
                return False
        

            for m, n in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if m >= 0 and m < len(board) and n >= 0 and n < len(board[0]) and visited[m][n] == 0:
                    visited[m][n] = 1
                    if rec_dfs(m,n,word[1:]):
                        return True
                    visited[m][n] = 0
                    
            return False
        
            
        visited = [[0] * len(board[0]) for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = 1
                if rec_dfs(i,j,word):
                    return True
                visited[i][j] = 0
        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(i, j, visited,  word):
            nonlocal res

            if not word:
                res = True
                return 

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[0]:
                return 


            visited[i][j] = True
            for next_i, next_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:

                search(next_i, next_j, visited, word[1:])
            
            visited[i][j] = False


        res = False
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    search(i,j, visited, word)

        return res
