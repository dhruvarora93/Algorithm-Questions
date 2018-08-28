class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def connect(root):
    stack = [root]
    next_pointers = []
    while stack:
        nodes = []
        while stack:
            node = stack.pop(0)
            nodes.append(node)

        next_pointers.append(nodes)
        for node in nodes:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return next_pointers


def right_side_view(root):
    if root:
        right_view = []
        next_pointers = connect(root)
        for i in next_pointers:
            right_view.append(i[-1].val)

        return right_view

    return []

a = TreeNode(10)
b = TreeNode(9)
c = TreeNode(8)
d = TreeNode(7)
e = TreeNode(6)
f = TreeNode(5)
g = TreeNode(4)

a.left = b
b.left = c
a.right = d
d.right = e
e.left = f
e.right = g

print(right_side_view(a))