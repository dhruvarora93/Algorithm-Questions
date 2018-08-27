import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    head = point = ListNode(0)
    h = []
    for value in lists:
        if value:
            heapq.heappush(h, (value.val,value))
    while h:
        value, node = heapq.heappop(h)
        point.next = ListNode(value)
        point = point.next
        node = node.next
        if node:
            heapq.heappush(h, (node.val, node))
    return head.next


a = ListNode(0)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
d.next = e

f = ListNode(64)
g = ListNode(65)
f.next = g
lists = [a,d,f]
head = merge_k_lists(lists)
while head:
    print(head.val)
    head = head.next


# Time Complexity: O(Nlogk), k = number of lists, n = total number of nodes
