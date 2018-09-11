import collections
class Solution(object):


    def cutOffTree(self, G):

        if not G or not G[0]: return -1
        m, n = len(G), len(G[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if G[i][j] > 1:
                    trees.append((G[i][j], i, j))
        trees = sorted(trees)
        count = 0
        cx, cy = 0, 0
        for _, x, y in trees:
            step = self.BFS(G, cx, cy, x, y)
            if step == -1:
                return -1
            else:
                count += step
                G[x][y] = 1
                cx, cy = x, y
        return count

    def BFS(self, G, cx, cy, tx, ty):
        m, n = len(G), len(G[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        Q = collections.deque()
        step = -1
        Q.append((cx, cy))
        while len(Q) > 0:
            step += 1
            x, y = Q.popleft()
            visited[x][y] = True
            if x == tx and y == ty:
                return step
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y-1), (x, y + 1)]:
                if nx < 0 or nx >= m or ny < 0 or ny >= n or G[nx][ny] == 0 or visited[nx][ny]:
                    continue
                Q.append((nx, ny))
        return -1