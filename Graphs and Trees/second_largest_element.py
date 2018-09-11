class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right




bt1 = BinaryTreeNode(5)
bt2 = BinaryTreeNode(3)
bt3 = BinaryTreeNode(8)
bt4 = BinaryTreeNode(1)
bt5 = BinaryTreeNode(4)
bt6 = BinaryTreeNode(7)
bt7 = BinaryTreeNode(12)
bt8 = BinaryTreeNode(10)
bt9 = BinaryTreeNode(9)
bt10 = BinaryTreeNode(11)

bt2.left = bt4
bt2.right = bt5

bt1.left = bt2

bt8.left = bt9
bt8.right = bt10

bt7.left = bt8
bt3.right = bt7
bt3.left = bt6
bt1.right = bt3


print(find_second_largest(bt1))

