class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key


def insert(root,node):
    if root is None:
        root = node
    else:
       if node.value < root.value:
           if root.left is None:
               root.left=node
           else:
                insert(root.left,node)
       else:
           if root.right is None:
               root.right = node
           else:
                insert(root.right,node)


def all_sequences(node):
    result = []
    if node is None:
        result.append([])
        return result

    prefix = []
    prefix.append(node.value)
    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)
    for l in left_seq:
        for r in right_seq:
            weaved = []
            weavelists(l,r,weaved,prefix)
            result.extend(weaved)
    return result


def weavelists(first,second,results,prefix):

    if len(first) == 0 or len(second) == 0:
        result = list(prefix)
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    head_first = first.pop(0)
    prefix.append(head_first)
    weavelists(first,second,results,prefix)
    prefix.pop()
    first.insert(0,head_first)

    head_second = second.pop(0)
    prefix.append(head_second)
    weavelists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)




root = Node(2)
n1 = Node(3)
n2 = Node(1)
n3 = Node(4)
root.left = n2
root.right = n1
n1.right = n3

print(all_sequences(root))

