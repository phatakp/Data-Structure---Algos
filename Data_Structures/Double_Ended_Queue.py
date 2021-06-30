# O(1) enqueue operation
# O(n) search operation
# O(1) dequeue operation

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


class DoubleEndedQueue:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items:
            _ = [self.add_at_tail(item) for item in items]

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

    def add_at_head(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        else:
            self.head.prev = node
            node.next = self.head
            self.make_head(node)

    def add_at_tail(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        else:
            self.tail.next = node
            node.prev = self.tail
            self.make_tail(node)

    def remove_at_head(self):
        if self.is_empty:
            return 'Queue is Empty'
        else:
            node = self.head
            self.make_head(node.next)
            node.next = None
            node.prev = None
            return node

    def remove_at_tail(self):
        if self.isempty:
            return 'queue is Empty'
        else:
            node = self.tail
            self.make_tail(node)
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
    from time import sleep
    from random import randint
    queue = DoubleEndedQueue()

    for _ in range(3):
        num = randint(1, 99)
        sleep(1)
        print('\nAdding at head:', num)
        queue.add_at_head(num)
        print(queue)
        sleep(1)
        print('\nAdding at tail:', num-1)
        queue.add_at_tail(num-1)
        print(queue)
