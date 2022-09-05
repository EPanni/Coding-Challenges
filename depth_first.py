""" Depth First Algorithm in Python"""


def depth_first_print(graph, source_node: str):
    """Main Function"""
    stack = [source_node]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

depth_first_print(graph, "a")
