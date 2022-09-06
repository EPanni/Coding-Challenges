""" Algorithm to find if it is possible the destination X when staring by Y """

graph = {"f": ["g", "i"], "g": "h", "h": "", "i": ["k", "g"], "j": "i", "k": ""}


def has_path(graph, src: str, dest: str):
    """Funtion based on depth first"""
    if src == dest:
        return True
    queue = [src]
    while queue:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def has_path_recur(graph, src: str, dest: str):
    """Funtion based on depth first - Recursively"""
    if src == dest:
        return True
    for neighbor in graph[src]:
        if has_path_recur(graph, neighbor, dest):
            return True
    return False


if __name__ == "__main__":
    print(has_path(graph, "f", "h"))
    print(has_path_recur(graph, "f", "h"))
