class LinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):
    def __init__(self, capacity):
        self.d = {}
        self.head = LinkedListNode(0,0)
        self.tail = LinkedListNode(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.capacity = capacity

    def get(self,key):
        if key not in self.d:
            return -1
        node = self.d[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self,key,value):
        if key in self.d:
            node = self.d[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            new_node = LinkedListNode(key,value)
            self.d[key] = new_node
            self._add(new_node)
            if len(self.d) > self.capacity:
                node = self.tail.previous
                self._remove(node)
                key = node.key
                self.d.pop(key)
        return

    def _remove(self, node):
        p1 = node.next
        p2 = node.previous
        p2.next = p1
        p1.previous = p2
        return

    def _add(self,node):
        p1 = self.head.next
        self.head.next = node
        p1.previous = node
        node.next = p1
        node.previous = self.head
        return


l = LRU_Cache(4)
l.put(1,2)
l.put(2,3)
l.put(3,4)
print(l.get(1))
l.put(4,5)
l.put(5,6)
print(l.get(2))
