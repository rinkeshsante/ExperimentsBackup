


def isSafe(row,col,board):
    
    # on x axis
    for i in range(col):
        if board[row][i]==1:
            return False
    # digonally up
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    # digonally down
    for i, j in zip(range(row,len(board),1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True

def solve(col,board):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if isSafe(i,col,board):
            board[i][col]=1
            if solve(col+1,board):
                return True
            else:
                board[i][col]=0
    
    return False



N = int(input('enter the dimentions of arr :'))
if 0< N < 10:
    arr = [[0 for i in range(N)] for j in range(N)]
    print(solve(0,arr))
    for y in arr:
        print(y)
 
