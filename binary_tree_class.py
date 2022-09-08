# Raw example


class Node:
    """It representes a node in a tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Example
a = Node(1)
b = Node(3)
c = Node(10)
d = Node(15)
e = Node(19)

a.right = b
a.left = c
b.left = d
b.left = e
