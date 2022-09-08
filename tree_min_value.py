class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root):

    min = float("inf")

    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.val < min:
            min = current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return min


def tree_min_value_recur(root):
    if not root:
        return float("inf")
    left = tree_min_value(root.left)
    right = tree_min_value(root.right)
    return min(root.val, left, right)


if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    print(tree_min_value(a))  # -> -2
    print(tree_min_value_recur(a))  # -> -2
