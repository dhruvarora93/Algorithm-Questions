def mark_locations(matrix, row, col):

    row_len = len(matrix[row])
    col_len = len(matrix)

    for i in range(row_len):
        if matrix[row][i] != 0:
            matrix[row][i] = '#'

    for j in range(col_len):
        if matrix[j][col] != 0:
            matrix[j][col] = '#'


def set_zeros(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                mark_locations(matrix,i,j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                matrix[i][j] = 0

    print(matrix)

mat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
set_zeros(mat)