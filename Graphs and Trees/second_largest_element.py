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

def find_second_largest(root_node):
    if root_node.right.right:
        return find_second_largest(root_node.right)

    elif root_node.right.left:
        return find_rightmost(root_node.right.left)

    else:
        return root_node

def find_rightmost(root):
    while root.right:
        return find_rightmost(root.right)

    return root




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

#bt7.left = bt8
bt3.right = bt7
bt3.left = bt6
bt1.right = bt3


print(find_second_largest(bt1).value)

