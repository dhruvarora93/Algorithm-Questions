class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def print_values(node):
    while node is not None:
        print(node.value)
        node = node.next


def delete_node(node):
    new_node = None
    if node.next:
        new_node = LinkedListNode(node.next.value)
        new_node.next = node.next.next

    return new_node


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
new_node = delete_node(b)
b = new_node
print_values(a)




