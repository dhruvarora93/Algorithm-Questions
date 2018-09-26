def exist(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited = [[False] * len(board[0]) for _ in range(len(board))]
            if dfs(board, i, j, word,visited):
                return True

    return False


def dfs(board, i, j, word,visited):

    if len(word) == 0: # all the characters are checked
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j] or visited[i][j]:
        return False

    #tmp = board[i][j]  # first character is found, check the remaining part
    #board[i][j] = "#"
    # avoid visit agian
    # check whether can find "word" along one direction
    visited[i][j] = True

    return dfs(board, i+1, j, word[1:],visited) or dfs(board, i-1, j, word[1:],visited) \
        or dfs(board, i, j+1, word[1:],visited) or dfs(board, i, j-1, word[1:],visited)

    visited[i][j] = False



board = \
[
  ['C','A','A'],
  ['A','A','A'],
  ['B','C','D']
]

print(exist(board,"CAB"))
