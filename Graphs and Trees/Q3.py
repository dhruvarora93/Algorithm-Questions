
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key


def create_list_dfs(lists,root,level):
    if root is None:
        return

    if len(lists) == level:
        lst = []
        lists.append(lst)
    else:
        lst=lists[level]

    lst.append(root.value)
    create_list_dfs(lists,root.left,level+1)
    create_list_dfs(lists, root.right, level + 1)
    return lists

def create_list_bfs(root):
    lst=[]
    lists=[]

    if root is not None:
        lst.append(root)



    while len(lst) > 0:
        lists.append(lst)
        parents=lst
        lst=[]
        for node in parents:
            if(node.left is not None):
                lst.append(node.left)

            if (node.right is not None):
                lst.append(node.right)

    return lists


def nodes_at_level(root,lst,cure_level,target):

    if root is None:
        return

    if cure_level == target:
        lst.append(root.value)

    nodes_at_level(root.left,lst,cure_level + 1,target)
    nodes_at_level(root.right,lst,cure_level + 1, target)
    return lst




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.right=Node(10)
result  = []
print(nodes_at_level(root,result,0,4))






