class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.parent=None
        self.value=key


def depth(n):
    height = 0
    while(n.parent):
        n = n.parent
        height += 1
    return height


def go_up(n,steps):
    count = 0
    while count != steps:
        n = n.parent
        count += 1
    return n

def find_succesor(n1,n2):
    n1_height = depth(n1)
    n2_height = depth(n2)
    height_diff = abs(n1_height-n2_height)
    if n2_height > n1_height:
        n2 = go_up(n2,height_diff)
    else:
        n1 = go_up(n1, height_diff)

    while n1 != n2 and n1 is not None and n2 is not None:
        n1 = n1.parent
        n2 = n2.parent

    return n1

def find_succesor1(n1,n2):
    n1_height = depth(n1)
    n2_height = depth(n2)

    height_diff = abs(n1_height - n2_height)
    if n2_height > n1_height:
        deeper_node = n2
        shallow_node = n1
    else:
        deeper_node = n1
        shallow_node = n2








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
print(find_succesor(root.right.left,root.left.left).value)