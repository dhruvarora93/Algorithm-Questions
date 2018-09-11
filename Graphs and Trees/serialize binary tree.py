class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def serialize(root):
        stack = [root]
        code = ''
        while stack:
            node = stack.pop()
            if node:
                code += '#' + str(node.val)
                stack.extend([node.right, node.left])
            else:
                code += '#$'
        return code

def serialize_recursive(root,output):
    if not root:
        output.append(None)
        return

    output.append(root.val)
    serialize_recursive(root.left,output)
    serialize_recursive(root.right,output)


def deserialize_recursive(numIter):
    val = next(numIter)
    if not val:
        return None

    node = Node(val)
    node.left = deserialize_recursive(numIter)
    node.right = deserialize_recursive(numIter)
    return node


def deserialize(data):
        val = iter.next()
        data = data[1:].split('#')[::-1]
        print(data)
        val = data.pop()
        cur = root = Node(int(val)) if val != '$' else None
        stack = [root]
        while data:
            val = data.pop()
            while data and val != '$':
                cur.left = Node(int(val))
                cur = cur.left
                stack.append(cur)
                val = data.pop()
            while data and val == '$':
                cur = stack.pop()
                val = data.pop()
            if data:
                cur.right = Node(int(val))
                cur = cur.right
                stack.append(cur)

        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right=Node(10)
lst = []
serialize_recursive(root,lst)
iterator = iter(lst)
#print(lst)
r = deserialize_recursive(iterator)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

inorder(r)
