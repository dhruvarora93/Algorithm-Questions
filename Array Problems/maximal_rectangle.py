def maximal_rectangle(matrix):

    horizontal_table = [[0] * len(matrix[0]) for _ in range(matrix)]
    vertical_table = [[0] * len(matrix[0]) for _ in range(matrix)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and matrix:
                horizontal_table[i][j] = max(check_ones(i,j + 1,0,matrix))
                vertical_table[i][j] = max(check_ones(i+1,j,1,matrix))


def check_ones(row,col,flag,matrix):
    count = 0
    if flag == 0:
        while col < len(matrix[row]):
            if matrix[row][col] == 1:
                count += 1
                col += 1
    else:
        while row < len(matrix):
            if matrix[row][col] == 1:
                count += 1
                row += 1

    return count


def largest_rectangle(heights,start,end,maximum):
    if start > end or start < 0 or end >= len(heights):
        return

    if start == end:
        maximum[0] = max(maximum[0],heights[start])
        return

    min_height_index = start
    for i in range(start,end+1):
        if heights[i] < heights[min_height_index]:
            min_height_index = i
    min_height = heights[min_height_index]
    maximum[0] = max(maximum[0],min_height * (end-start+1))
    largest_rectangle(heights,start, min_height_index - 1, maximum)
    largest_rectangle(heights, min_height_index + 1, end, maximum)

def helper(heights):
    maximum = [float('-inf')]
    largest_rectangle(heights, 0, len(heights) - 1, maximum)
    return maximum[0]



print(helper([1,2,3]))







