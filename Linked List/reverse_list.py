class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def print_values(node):
    while node is not None:
        print(node.value)
        node = node.next


def reverse(head):
    if not head:
        return None
    if not head.next:
        return head
    current = head
    end = head.next
    middle = head
    while end:
        middle.next = end.next
        end.next = current
        current = end
        end = middle.next

    return current


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
a.next = b
b.next = c
new = reverse(a)
print_values(new)