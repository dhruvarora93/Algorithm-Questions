class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

    def mirror(self):

        if root is None:
            return

        queue = []
        queue.append(root)

        while queue:

            node = queue.pop(0)
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



def inorder(root):
    if root:
        print(root.value,end=" ")
        inorder(root.left)
        inorder(root.right)


def build_tree(preorder,inorder):

    if len(preorder) == 0:
        return None

    root_node = Node(preorder[0])
    index = inorder.index(preorder[0])
    root_node.left = build_tree(preorder[1:index+1],inorder[0:index])
    root_node.right = build_tree(preorder[index+1:],inorder[index+1:])
    return root_node


def build_tree1(postorder,inorder):

    if len(postorder) == 0:
        return None

    last = postorder.pop()
    root2 = Node(last)
    index = inorder.index(last)
    root2.left = build_tree1(postorder[:index], inorder[:index])
    root2.right = build_tree1(postorder[index:], inorder[index + 1:])
    return root2






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.right=Node(10)
#inorder(root)
#root.mirror()
#inorder(root)
inorder1 = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]
root1 = build_tree1(postorder,inorder1)
inorder(root1)
