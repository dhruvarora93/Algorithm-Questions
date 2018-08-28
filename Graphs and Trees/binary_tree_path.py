class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def binary_path(root):

    if not root:
        return []

    result = []

    def dfs(root, ans=''):
        ans += str(root.key)
        if root.left is None and root.right is None:
            result.append(ans)
            return

            #return

        #ans += '->'

        if root.left:
            dfs(root.left,ans)
        if root.right:
            dfs(root.right,ans)

    dfs(root)

    return sum(int(i) for i in result)


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.right = Node(5)

print(binary_path(r))
