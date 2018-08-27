def solve(board):
    record = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1) and board[i][j] == 'O':
                dfs(board,i,j,record)

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 'X'

    for r,c in record:
        board[r][c] = 'O'

    print(board)


def dfs(board,row,col,record):

    if row in range(len(board)) and col in range(len(board[row])) and board[row][col] == 'O':
        board[row][col] = '#'
        record.append((row,col))
        dfs(board,row+1,col,record)
        dfs(board,row-1,col,record)
        dfs(board,row,col+1,record)
        dfs(board,row,col-1,record)




board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
solve(board)



