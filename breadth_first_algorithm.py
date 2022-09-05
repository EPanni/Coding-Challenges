""" Breadth First Algorithm in Python [Recursively] """

# Input
graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def breadth_list_print(graph, source_node: str):
    """Breadth"""
    queu = [source_node]
    while queu:
        current = queu.pop(0)
        print(current)
        for neighbor in graph[current]:
            queu.append(neighbor)


breadth_list_print(graph, "a")
