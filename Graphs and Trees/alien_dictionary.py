from collections import defaultdict


class Graph:

    def __init__(self,v):
        self.graph = defaultdict(set)
        self.state=defaultdict(None)
        self.vertices=v
        for v in self.vertices:
            self.state[v]='Blank'

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def find_build_oder(self):
        order=[]
        for v in self.vertices:

            if(self.state[v]=='Blank'):
                if self.dfs(v,order):
                   pass
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


words = [
  'z','x','z'
]
unique_letters = []
for word in words:
    unique_letters.extend(list(set(word)))

unique_letters = list(set(unique_letters))

g = Graph(unique_letters)


pos1, pos2 = 0, 1
while pos1 < pos2 < len(words):
    w1 = words[pos1]
    w2 = words[pos2]
    len1 = len(w1)
    len2 = len(w2)
    st = 0
    while st < min(len1, len2):
        if w1[st] != w2[st]:
            g.addEdge(w1[st],w2[st])
        st += 1
    pos1 += 1
    pos2 += 1
print(g.find_build_oder())