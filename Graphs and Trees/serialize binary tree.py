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

def deserialize(data):
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

code = serialize(root)
r = deserialize(code)
