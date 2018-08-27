

def get_max_reward(mat, row, col):

    if row < 0 or col < 0:
        return 0

    else:
        return mat[row][col] + max(get_max_reward(mat,row-1,col),get_max_reward(mat,row,col-1))


def get_reward(mat):

    reward = [[0]*len(mat[0]) for _ in range(len(mat))]
    visited = [[False]*len(mat[0]) for _ in range(len(mat))]
    temp = 0
    dfs(mat,0,0,visited,reward,temp)
    print(reward)
    return reward[len(mat)-1][len(mat[0])-1]

def dfs(mat,start,end,visited,reward,temp):

    if start in range(len(mat)) and end in range(len(mat[0])) and not visited[start][end]:
        visited[start][end] = True
        temp1 = temp + mat[start][end]
        temp = max(temp, temp1)
        dfs(mat,start+1,end,visited,reward,temp)
        dfs(mat,start,end+1,visited,reward,temp)
        reward[start][end] = temp


mat = [[1,2,3],[9,-8,7],[4,5,6]]
cost = [[0]*len(mat[0])]*len(mat)
print(get_reward(mat))