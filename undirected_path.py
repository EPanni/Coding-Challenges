"""From Structy

# undirected path

Write a function, undirected_path, that takes in a list of edges for an 
undirected graph and two nodes (node_A, node_B). The function should return a
boolean indicating whether or not there exists a path between node_A 
and node_B.

test_00:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
"""


def convert_to_graph(edges_list: list) -> dict:
    """Aux function to convert the input"""
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


def has_path(graph, src, dest, visit) -> bool:
    """It checks if there ia a path between a and b / marks the visited nodes and returns a boolean"""
    if src in visit:
        return False

    if src == dest:
        return True

    visit.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest, visit):
            return True
    return False


def undirected_path(edges, node_A, node_B) -> bool:

    graph = convert_to_graph(edges)
    conj = set()  # To handle infinite loops
    return has_path(graph, node_A, node_B, conj)


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

a = undirected_path(edges, "l", "j")  # -> True
print(a)
