class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key


def balanced_tree(root):
    if root is None:
        return 0

    ans1=balanced_tree(root.left)
    if ans1==-1:
        return -1
    ans2=balanced_tree(root.right)
    if ans2==-1:
        return -1

    if abs(ans1-ans2)>1:
        return -1
    else:
        return max(ans1,ans2)+1


def insert(root,node):
    if root is None:
        root=node
    else:
       if node.value < root.value:
           if root.left is None:
               root.left=node
           else:
                insert(root.left,node)
       else:
           if root.right is None:
               root.right=node
           else:
                insert(root.right,node)

def find_height(root):

    if balanced_tree(root)!=-1:
        return True
    return False


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


ar = [0,1,2,3,5,6,7,8,9,10]
root = create_tree_min_height(ar)
node=Node(4)
insert(root,node)
print(find_height(root))

