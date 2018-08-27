class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key


class Codec:

    def serialize(self,root,s):

        if not root:
            s.append('/ ')
            return

        s.append(str(root.value)+' ')
        self.serialize(root.left,s)
        self.serialize(root.right,s)


    def serializer(self,root):

        s = []
        self.serialize(root,s)
        return ''.join(s)

    def deserialize(self,string):
        data = string.split(" ")
        index = [0]
        return self.deserializer(data,index)

    def deserializer(self,ar,index):
        if index[0] > len(ar):
            return None
        if ar[index[0]] == '/':
            return None
        node = Node(int(ar[index[0]]))
        index[0] += 1
        node.left = self.deserializer(ar,index)
        index[0] += 1
        node.right = self.deserializer(ar, index)
        return node

    def inorder(self,root):
        current = root
        stack = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                print(node.value)
                current = node.right





root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)

c=Codec()
#print(c.serializer(root))
node = c.deserialize(c.serializer(root))
c.inorder(node)


