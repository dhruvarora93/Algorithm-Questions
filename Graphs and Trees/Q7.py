from collections import defaultdict


class Graph:

    def __init__(self,v):
        self.graph = defaultdict(list)
        self.state=defaultdict(None)
        self.vertices=v
        for v in self.vertices:
            self.state[v]='Blank'

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_build_oder(self):
        order=[]
        for v in self.vertices:

            if(self.state[v]=='Blank'):
                if(self.dfs(v,order)==False):
                    return None
        return order

    def dfs(self,v,order):
        if self.state[v]=='Partial':
            return False   # Cycle is present

        if self.state[v]=='Blank':
            self.state[v]='Partial'
            children=self.graph[v]
            for child in children:
                if (self.dfs(child, order) == False):
                    return False

            self.state[v]='Complete'
            order.insert(0,v)
        return True

projects=['a','b','c','d','e','f']
g=Graph(projects)
g.addEdge('a','d')
g.addEdge('f','b')
g.addEdge('b','d')
g.addEdge('f','a')
g.addEdge('d','c')
print(g.find_build_oder())



