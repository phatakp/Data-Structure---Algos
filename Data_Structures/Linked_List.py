# O(1) add operation
# O(n) search operation
# O(n) remove operation

class Node:
    def __init__(self, value):
        self.value = value
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items:
            _ = [self.add(item) for item in items]

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

    def make_head(self, node):
        node.next = self.head
        self.head = node

    def make_tail(self, node):
        if self.tail:
            self.tail.next = node
        self.tail = node

    def add_at_head(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        else:
            self.make_head(node)

    def add_at_tail(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        else:
            self.make_tail(node)

    def add(self, value):
        return self.add_at_tail(value)

    def find(self, value):
        for node in iter(self):
            if node.value == value:
                return node

    def remove(self, value):
        prev_node = None
        for node in iter(self):
            if node.value != value:
                prev_node = node
            else:
                if prev_node:
                    if self.is_tail(node):
                        self.make_tail(prev_node)
                    prev_node.next = node.next
                else:
                    # Node to remove is head
                    self.make_head(node.next)
                node.next = None
                return f"Node with {value=} removed"

        return f"Node not found with {value=}"

    @property
    def is_empty(self):
        return self.head is None

    def is_head(self, node):
        return self.head == node

    def is_tail(self, node):
        return self.tail == node

    def __str__(self):
        def line(num):
            if num in (0, 4):
                return "   ".join(['-'*11 for _ in iter(self)])
            elif num == 1:
                return "   ".join([f'|{node.value:^9}|' for node in iter(self)])
            elif num == 2:
                return "==>".join(['-'*11 for _ in iter(self)])
            else:
                return "   ".join([f'|Next:{node.next.value:^4}|' if node.next else '|Next:None|' for node in iter(self)])

        return '\n'.join([line(i) for i in range(5)])


if __name__ == '__main__':
    from time import sleep
    from random import randrange
    linked_list = LinkedList()

    for _ in range(5):
        sleep(2)
        num = randrange(100)
        if num % 2 == 0:
            print('\nAdding at head:', num)
            linked_list.add_at_head(num)
        else:
            print('\nAdding at tail:', num)
            linked_list.add_at_tail(num)
        print(linked_list)
