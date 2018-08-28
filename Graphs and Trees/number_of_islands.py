def dfs(row, col, visited, grid):
    if (row in range(len(grid)) and col in range(len(grid[row])) and not visited[row][col] and grid[row][col] == '1'):
        visited[row][col] = True
        dfs(row, col - 1, visited, grid)
        dfs(row, col + 1, visited, grid)
        dfs(row - 1, col, visited, grid)
        dfs(row + 1, col, visited, grid)


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1' and not visited[row][col]:
                dfs(row, col, visited, grid)
                islands += 1
    return islands

print(numIslands([["1","1","1"],["1","0","1"],["1","1","1"]]))