from collections import deque


def bfs(graph, start_node, end_node):
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)
    shortest_path = {start_node: None}
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()
        if current_node == end_node:
            return reconstruct_path(shortest_path, end_node)
            # Found it!

        for neighbor in graph[current_node]:
            if (neighbor not in shortest_path and neighbor in graph) or neighbor == end_node:
                nodes_to_visit.append(neighbor)
                shortest_path[neighbor] = current_node

    return 'No path exists'


def reconstruct_path(shortest_path, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = shortest_path[current]

    return path[::-1]


network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],

}

print(bfs(network,'Jayden','Miguel'))






