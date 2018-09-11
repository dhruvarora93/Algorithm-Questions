class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def distanceK(root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    parents = {root: None}

    def annotate_parents(root, parents):
        if root.left:
            parents[root.left] = root
            annotate_parents(root.left, parents)

        if root.right:
            parents[root.right] = root
            annotate_parents(root.right, parents)

    annotate_parents(root, parents)
    nodes = []
    queue = [(target,0)]
    seen = set()
    while queue:

        item = queue.pop(0)
        node = item[0]
        distance = item[1]
        seen.add(node)

        if distance == K:
            nodes.append(node.val)
            continue

        if parents[node] and parents[node] not in seen:
            queue.append((parents[node], distance + 1))

        if node.left and node.left not in seen:
            queue.append((node.left, distance + 1))

        if node.right and node.right not in seen:
            queue.append((node.right, distance + 1))

    print(nodes)

a = TreeNode(10)
b = TreeNode(9)
c = TreeNode(8)
d = TreeNode(7)
e = TreeNode(6)
f = TreeNode(5)
g = TreeNode(4)

a.left = b
b.left = c
a.right = d
d.right = e
e.left = f
e.right = g

distanceK(a,a,2)
