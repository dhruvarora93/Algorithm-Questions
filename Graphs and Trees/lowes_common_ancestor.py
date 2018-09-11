class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if findPath(root.left, path, k) or findPath(root.right, path, k):
        return True

    path.pop()
    return False


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    path1 = []
    path2 = []
    if not findPath(root, path1, p) or not findPath(root, path2, q):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


def lca(root,node1,node2):
    if root.key > node1 and root.key > node2:
        return lca(root.left,node1,node2)
    elif root.key < node1 and root.key < node2:
        return lca(root.right,node1,node2)
    else:
        return root.key



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print ("LCA(4, 5) = %d" %(lca(root, 4, 5)))
print ("LCA(4, 6) = %d" %(lowestCommonAncestor(root, 4, 6)))
print ("LCA(3, 4) = %d" %(lowestCommonAncestor(root,3,4)))


