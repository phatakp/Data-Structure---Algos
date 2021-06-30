# O(n) add operation
# O(n) search operation
# O(n) remove operation

from bisect import bisect_left


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


class SortedLinkedList:
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
        node.prev = None
        self.head = node

    def make_tail(self, node):
        node.next = None
        self.tail = node

    def _add_at_head(self, node):
        self.head.prev = node
        node.next = self.head
        self.make_head(node)

    def _add_at_tail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.make_tail(node)

    def find_position(self, value):
        node = self.head
        pos = 0
        while node and node.value <= value:
            node = node.next
            pos += 1
        return node, pos

    def add(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_head(node)
            self.make_tail(node)
        elif node.value < self.head.value:
            self._add_at_head(node)
        elif node.value >= self.tail.value:
            self._add_at_tail(node)
        else:
            next_node, pos = self.find_position(node.value)
            if not next_node:
                self._add_at_tail(node)
            else:
                next_node.prev.next = node
                node.prev = next_node.prev
                node.next = next_node
                next_node.prev = node

    def find(self, value):
        for node in iter(self):
            if node.value == value:
                return node

    def remove(self, value):
        node_to_remove = self.find(value)

        if not node_to_remove:
            return f"Node not found with {value=}"

        if self.is_head(node_to_remove) and node_to_remove.next:
            self.make_head(node_to_remove.next)
        elif self.is_tail(node_to_remove):
            self.make_tail(node_to_remove.prev)
        else:
            node_to_remove.prev.next = node_to_remove.next
            node_to_remove.next.prev = node_to_remove.prev

        node_to_remove.next = None
        node_to_remove.prev = None
        return f"Node with {value=} removed"

    @property
    def is_empty(self):
        return self.head is None

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
    from random import randrange
    linked_list = SortedLinkedList([45, 23, 12, 7, 89])

    # for num in (45, 23, 12, 7, 89):
    #     sleep(2)
    #     print('\nAdding:', num)
    #     linked_list.add(num)
    print(linked_list)
    print(linked_list.remove(89))
    print(linked_list)
