


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key


def inorder(root):
    if root:
        inorder(root.left)
        numbers.append(root.value)
        inorder(root.right)
        return numbers


def create_tree_min_height(numbers):
    root= create_tree(numbers,0,len(numbers)-1)
    return root

def create_tree(numbers,start,end):
    if end<start:
        return None
    mid=int((start+end)/2)
    root=Node(numbers[mid])
    root.left=create_tree(numbers,start,mid-1)
    root.right=create_tree(numbers,mid+1,end)
    return root







ar = [20,30,40,50,60,70,80,90]
root = create_tree_min_height(ar)
numbers=[]
a=inorder(root)
a = Node(2)
a.left = Node(1)
a.right = Node(3)
print(check_bst(a))
#print(all(a[i+1]>a[i] for i in range(len(a)-1)))