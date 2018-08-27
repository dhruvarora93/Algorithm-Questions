class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right



def is_super_balanced(node):
    if node is None:
        return True

    depths = []

    nodes = []
    nodes.append((node,0))

    while len(nodes):
        n, d = nodes.pop()

        if node.left is None and node.right is None:
            if d not in depths:

                depths.append(d)

                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        else:
            if node.left:
                nodes.append((node.left, d+1))
            if node.right:
                nodes.append((node.right, d+1))

    return True
















