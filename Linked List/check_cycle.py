class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def check_cycle(node):
    if not node.next:
        return False
    head1 = node
    head2 = node.next
    while head1 != head2:
        if not head1.next:
            return False
        if not head2.next.next:
            return False
        head1 = head1.next
        head2 = head2.next.next

    return True


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = a
print(check_cycle(a))