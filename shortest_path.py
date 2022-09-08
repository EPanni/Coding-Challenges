"""shortest path
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

test_00:
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2
    """


def shortest_path(edges, node_A, node_B):
    graph = convert_to_graph(edges)
    queue = [[node_A, 0]]
    visited = set(node_A)

    while queue:
        node, dist = queue.pop(0)
        if node == node_B:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, dist + 1])
    return -1


def convert_to_graph(edges_list: list) -> dict:

    graph = {}

    for edge in edges_list:
        a, b = edge
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    return graph


if __name__ == "__main__":
    edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
    a = shortest_path(edges, "w", "z")  # -> 2
    print(a)
