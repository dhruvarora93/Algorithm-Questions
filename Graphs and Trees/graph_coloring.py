from collections import defaultdict
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def coloring(graph):
    distinct_colors = ['r','g','b','y']

    for node in graph:

        colors_used = set()

        for i in node.neighbors:
            if i == node:
                raise Exception('Cycle is present, no legal coloring possible')
            elif i.color:
                colors_used.add(i.color)

        for color in distinct_colors:
            if color not in colors_used:
                node.color = color
                break




a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
graph = [a,b,c]
coloring(graph)
for g in graph:
    print(g.color)