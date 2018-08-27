class Node:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    stack = [root]

    while stack:
        nodes = []
        while stack:
            node = stack.pop(0)
            nodes.append(node)
            if stack:
                node.next = stack[0]

        for node in nodes:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


def find_k_smallest(root,k):

    if not root:
        return 'Error: k > number of nodes'

    leaf_nodes = count_nodes(root.left)
    if k <= leaf_nodes:
        return find_k_smallest(root.left,k)

    if k == leaf_nodes + 1:
        return root.val

    return find_k_smallest(root.right, k-leaf_nodes-1)


def count_nodes(root):

    if root is None:
        return 0

    return count_nodes(root.left) + count_nodes(root.right) + 1


root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(13)

#connect(root)
print(find_k_smallest(root,7))