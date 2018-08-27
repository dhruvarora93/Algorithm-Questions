class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.parent=None
        self.value=key


def successor(node):
    if node.right:
        n = find_lefmost_node(node.right)
        return n
    else:
        p = node.parent
        while p is not None and p.left != node:
            node = p
            p = p.parent
        return p


def find_lefmost_node(node):
    while node.left:
        node=node.left
    return node



root = Node(10)
root.left = Node(8)
root.left.parent=root
root.right = Node(12)
root.right.parent=root
root.right.left=Node(11)
root.right.left.parent=root.right
root.right.right=Node(13)
root.right.right.parent=root.right
root.left.left = Node(7)
root.left.left.parent=root.left
root.left.right = Node(9)
root.left.right.parent=root.left
root.left.left.left=Node(6)

print(successor(root.left.right).value)

