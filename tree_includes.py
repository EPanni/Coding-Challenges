import re


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):

    if not root:
        return False
    queue = [root]

    while queue:
        current = queue.pop(0)

        print(current.val)

        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

        return False


def tree_includes_recur(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    left = tree_includes_recur(root.left, target)
    right = tree_includes_recur(root.right, target)

    return left or right
