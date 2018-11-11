##  思路


- 遍历整张图，从每个位置开始DFS看是否能够构成结果字符串
- rec_dfs 的终止条件为：
    - word 只剩下一个字符且与当前位置的字符相等, 返回True
    - 如果当前位置的字符与字符串的第一个字符不等，返回False

```Python
class Solution:
    def exist(self, board, word):

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
```