def search_a_matrix(mat,target):

    row_index = len(mat) - 1
    column_index = 0
    while row_index in range(len(mat)) and column_index in range(len(mat[row_index])):

        if mat[row_index][column_index] == target:
            return True

        elif target > mat[row_index][column_index]:
            column_index += 1

        else:
            row_index -= 1

    return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(search_a_matrix(matrix,5))