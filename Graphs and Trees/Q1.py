from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s, t):
        visited = [False] * (len(self.graph))
        queue = []
        visited[s] = True
        queue.append(s)

        while queue:

            node = queue.pop(0)

            for i in self.graph[node]:
                if visited[i] == False:
                    if i == t:
                        return True
                    else:
                        visited[i] = True
                        queue.append(i)
        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.bfs(3, 1))
