class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def kth_to_last_node(index, head):
    temp = head
    length = 1
    while temp.next:
        length += 1
        temp = temp.next
    count = 0
    while count != length - index:
        head = head.next
        count += 1
    print(head.value)


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

kth_to_last_node(3, a)