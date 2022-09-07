def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        if walk_through(graph, node, visited):
            count += 1
    return count


def walk_through(graph: dict, src: str, visited: set) -> bool:
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        walk_through(graph, neighbor, visited)
    return True


if __name__ == "__main__":
    input = {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
    print(connected_components_count(input))
