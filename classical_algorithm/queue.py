def check1(board,pos):
    x,y = pos
    for i in range(x):
        for j in range(len(board)):
            if board[i][j] == 1:
                if j == y or abs(j-y) == abs(i-x):
                    return False
    return True

def eightqueue1(board,row):
    if row == len(board):    # 来到不存在的第九行了
        print(board)
        return 

    for y in range(len(board)):
        if check1(board,(row,y)):
            board[row][y] = 1   
            eightqueue1(board,row+1)   
            board[row][y] = 0
    
    return False


## 优化
def check2(board,row,col):
    



def eightqueue2(board,row):
    if row == len(board):
        print(board)
        return 

    for col in range(len(board)):
        if check(board,row,col):
            board[row] = col
            eightqueue2(board,row+1)
            board[row] = 0
    return False






if __name__ == '__main__':
    board = [[0]*4 for i in range(4)]
    eightqueue1(board,0)