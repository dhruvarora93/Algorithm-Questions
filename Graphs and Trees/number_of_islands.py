def dfs(matrix,row, col, visited,indices,count):
    if (row in range(len(matrix)) and col in range(len(matrix[row])) and not visited[row][col] and matrix[row][col] == '1'):
        visited[row][col] = True
        count[0] += 1
        indices.append((row,col))
        dfs(row, col - 1, visited, matrix,indices,count)
        dfs(row, col + 1, visited, matrix, indices,count)
        dfs(row - 1, col, visited, matrix, indices,count)
        dfs(row + 1, col, visited, matrix, indices,count)


def find_largest_island(matrix):

    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    max_count = float('-inf')
    max_indices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '1' and not visited[row][col]:
                indices = []
                count = [0]
                dfs(row, col, visited, matrix,indices,count)
                last_count = max_count
                max_count = max(max_count,count[0])
                if last_count != max_count:
                    max_indices = indices

    rows = []
    columns = []
    for index in max_indices:
        rows.append(index[0])
        columns.append(index[1])
    bounding_box = [(min(rows),min(columns)),(max(rows),max(columns))]
    return max_count, bounding_box

print(find_largest_island([['0', '0', '1' ,'1' ,'0', '0', '0', '0', '0'],
                  ['0', '1', '1' ,'1' ,'1', '0', '1', '1', '0'],
                  ['1', '0', '0' ,'1' ,'0', '0', '1', '1', '0']]))