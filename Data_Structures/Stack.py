# O(1) push operation
# O(n) search operation
# O(1) pop operation

class Node:
    def __init__(self, value):
        self.value = value
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items:
            _ = [self.push(item) for item in items]

    def __contains__(self, value):
        return bool(self.find(value))

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        if self.node:
            item = self.node
            self.node = self.node.next
            return item
        else:
            raise StopIteration

    def __len__(self):
        count = 0
        for _ in iter(self):
            count += 1
        return count

    @property
    def is_empty(self):
        return self.head == None

    def make_head(self, node):
        node.prev = None
        self.head = node

    def make_tail(self, node):
        node.next = None
        self.tail = node

    def push(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        else:
            self.tail.next = node
            node.prev = self.tail
            self.make_tail(node)

    def pop(self):
        if self.is_empty:
            return 'Stack is Empty'
        else:
            node = self.tail
            self.make_tail(node.prev)
            node.next = None
            node.prev = None
            return node

    def find(self, value):
        for node in iter(self):
            if node.value == value:
                return node

    def is_head(self, node):
        return self.head == node

    def is_tail(self, node):
        return self.tail == node

    def __str__(self):
        def line(num):
            if num in (0, 5):
                return "   ".join(['-'*11 for _ in iter(self)])
            elif num == 1:
                return "   ".join([f'|{str(node):^9}|' for node in iter(self)])
            elif num == 2:
                return "<=>".join(['-'*11 for _ in iter(self)])
            elif num == 3:
                return "   ".join([f'|Prev:{str(node.prev):^4}|' if node.prev else '|Prev:None|' for node in iter(self)])
            else:
                return "   ".join([f'|Next:{str(node.next):^4}|' if node.next else '|Next:None|' for node in iter(self)])

        return '\n'.join([line(i) for i in range(6)])


if __name__ == '__main__':
    stack = Stack([4, 6, 2, 13, 7])
    print(stack)

    for _ in range(2):
        stack.pop()
        print(stack)
