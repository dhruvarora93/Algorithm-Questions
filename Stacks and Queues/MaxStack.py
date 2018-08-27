class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.maximum = float('-inf')
        self.list_of_max = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)
        if item > self.maximum:
            self.maximum = item
        self.list_of_max.append(self.maximum)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        item = self.items.pop()
        if item == self.maximum:
            self.list_of_max.pop()
            if not self.list_of_max:
                self.maximum = None
            else:
                self.maximum = self.list_of_max[-1]

        return item


    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        return self.maximum

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())



