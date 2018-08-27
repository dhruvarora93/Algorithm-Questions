class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

def insert(root,node):
    if root is None:
        root = node
    else:
       if node.value < root.value:
           if root.left is None:
               root.left=node
           else:
                insert(root.left,node)
       else:
           if root.right is None:
               root.right = node
           else:
                insert(root.right,node)


def create_tree_min_height(numbers):
    root = create_tree(numbers,0,len(numbers)-1)
    return root

def create_tree(numbers,start,end):
    if end < start:
        return None
    mid=int((start+end)/2)
    root=Node(numbers[mid])
    root.left=create_tree(numbers,start,mid-1)
    root.right=create_tree(numbers,mid+1,end)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,)
        inorder(root.right)

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.value,)


def postorder_iterative(root):

    first_stack = []
    second_stack = []
    first_stack.append(root)
    while first_stack:
        node = first_stack.pop()
        second_stack.append(node.value)
        if node.left:
            first_stack.append(node.left)
        if node.right:
            first_stack.append(node.right)
    print(second_stack[::-1])


def inorder_iterative(root):
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            print(node.value)
            current = node.right


def preorder_iterative(root):
    stack = list()
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



ar = [20,30,40,50,60,70,80]
r = create_tree_min_height(ar)
#postorder_recursive(r)
#postorder_iterative(r)
#inorder_iterative(r)
preorder_iterative(r)



