""" Depth First Algorithm in Python [Recursively] """

graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

# def depth_first_print(graph, source_node: str):
#    """Main Function"""
#    stack = [source_node]
#
#    while stack:
#        current = stack.pop()
#        print(current)
#
#        for neighbor in graph[current]:
#            stack.append(neighbor)


def depth_first_print(graph, source_node: str):
    """Recursively implementation"""
    print(source_node)
    for neighbor in graph[source_node]:
        depth_first_print(graph, neighbor)


depth_first_print(graph, "a")
