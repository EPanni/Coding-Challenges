""" Write a function, largest_component, that takes in the adjacency list of an
undirected graph. The function should return the size of the largest connected 
component in the graph.

test_00:
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4
"""


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        out = explorer(graph, node, visited)
        if out:
            if largest < out[1]:
                largest = out[1]
    return largest


def explorer(graph: dict, src: str, visited: set) -> list:
    aux = len(visited)
    if src in visited:
        return False
    visited.add(src)
    for node in graph[src]:
        explorer(graph, node, visited)
    output = [True, len(visited) - aux]
    return output


input = {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
a = largest_component(input)
print(a)
