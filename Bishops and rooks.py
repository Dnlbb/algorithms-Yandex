def update_rook_threats(board, threats, row, col):
    
    for i in range(col - 1, -1, -1):  
        if board[row][i] != '*':  
            break
        threats[row][i] = 1
    for i in range(col + 1, 8):  
        if board[row][i] != '*':  
            break
        threats[row][i] = 1

   
    for i in range(row - 1, -1, -1): 
        if board[i][col] != '*':  
            break
        threats[i][col] = 1
    for i in range(row + 1, 8):  
        if board[i][col] != '*':  
            break
        threats[i][col] = 1

def update_bishop_threats(board, threats, row, col):
   
    for i in range(1, 8):  
        if not (0 <= row-i < 8 and 0 <= col+i < 8) or board[row-i][col+i] != '*':
            break
        threats[row-i][col+i] = 1
    for i in range(1, 8): 
        if not (0 <= row-i < 8 and 0 <= col-i < 8) or board[row-i][col-i] != '*':
            break
        threats[row-i][col-i] = 1
    for i in range(1, 8):  
        if not (0 <= row+i < 8 and 0 <= col+i < 8) or board[row+i][col+i] != '*':
            break
        threats[row+i][col+i] = 1
    for i in range(1, 8): 
        if not (0 <= row+i < 8 and 0 <= col-i < 8) or board[row+i][col-i] != '*':
            break
        threats[row+i][col-i] = 1



def count_safe_cells(board):
    threats = [[0 for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                update_rook_threats(board, threats, i, j)
            elif board[i][j] == 'B':
                update_bishop_threats(board, threats, i, j)
    
    safe_cells = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == '*' and threats[i][j] == 0:
                safe_cells += 1
    
    return safe_cells

chessboard = list()

for i in range(8):
  chessboard.append(input())


print(count_safe_cells(chessboard))
