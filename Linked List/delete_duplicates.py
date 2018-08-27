class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def delete_duplicates(head):
    duplicates = set()
    if head is None or head.next is None:
        return head
    back = head
    front = head.next
    duplicates.add(back.value)
    while front:
        if front.value not in duplicates:
            duplicates.add(front.value)
            back = front
            front = front.next
        else:
            back.next = front.next
            front = back.next

    return head


a = LinkedListNode(8)
b = LinkedListNode(1)
c = LinkedListNode(3)
d = LinkedListNode(3)
e = LinkedListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
new_head = delete_duplicates(a)
while new_head:
    print(new_head.value)
    new_head = new_head.next