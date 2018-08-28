class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = p.next.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead


    def copy_using_map(self,head):
        map = {}
        iterNode = head
        while iterNode:
            map[iterNode] = RandomListNode(iterNode.label)
            iterNode = iterNode.next

        iterNode = head
        while iterNode:
            map[iterNode].next = map[iterNode.next] if iterNode.next else None
            map[iterNode].random = map[iterNode.random] if iterNode.random else None
            iterNode = iterNode.next
        return map[head] if head else None