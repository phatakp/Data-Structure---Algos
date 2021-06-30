"""
Self Balancing Binary Search Trees
Named after Georgy Adelson-Velsky and Evgenii Landis
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None    # Lesser value than parent
        self.right_child = None   # Equal or Greater value than parent

    # --------Methods----------------
    def add_left_child(self, child):
        self.left_child = child
        if child:
            child.add_as_parent(self)

    def add_right_child(self, child):
        self.right_child = child
        if child:
            child.add_as_parent(self)

    def add_as_parent(self, node):
        self.parent = node
        if self.value < node.value:
            node.left_child = self
        else:
            node.right_child = self

    def remove_left_child(self):
        self.left_child = None

    def remove_right_child(self):
        self.right_child = None

    def remove_children(self):
        self.remove_left_child()
        self.remove_right_child()

    def get_max_height(self, max_height=0):
        if self:
            if self.height > max_height:
                max_height = self.height
            if self.left_child:
                max_height = self.left_child.get_max_height(max_height)
            if self.right_child:
                max_height = self.right_child.get_max_height(max_height)
        return max_height

    # ------------ Additional Properties -------------------

    @property
    def height(self):
        # No of edges to the root + 1
        height = 0
        node = self
        while node.parent:
            height += 1
            node = node.parent
        return height

    @property
    def is_root(self):
        return self.height == 0 and self.parent is None

    @property
    def children(self):
        return len([node for node in (self.left_child, self.right_child) if node is not None])

    @property
    def left_tree_height(self):
        height = self.height
        if self.left_child:
            return self.left_child.get_max_height(height)
        return height

    @property
    def right_tree_height(self):
        height = self.height
        if self.right_child:
            return self.right_child.get_max_height(height)
        return height

    @property
    def balance_factor(self):
        return self.right_tree_height - self.left_tree_height

    @property
    def is_left_heavy(self):
        return self.balance_factor < 0

    @property
    def is_right_heavy(self):
        return self.balance_factor > 0

    @property
    def is_left_child_of_parent(self):
        return self.value < self.parent.value

    @property
    def is_right_child_of_parent(self):
        return not self.is_left_child_of_parent

    @property
    def has_no_children(self):
        return self.children == 0

    @property
    def has_both_children(self):
        return self.children == 2

    def __str__(self):
        return str(self.value)


class AVLTree:

    def __init__(self, items=None):
        self.root = None

        # Below properties are not related to AVL Tree
        # They are just used for printing of nodes in Command line
        self.nodes = []   # Used just as db storage for nodes
        self.nodes_added = set()  # used to add nodes to correct pos in db
        if items:
            _ = [self.add(item) for item in items]

    @property
    def is_empty(self):
        return self.root == None

    @property
    def height(self):
        # Distance of farthest child node of root
        return self.root.get_max_height()

    def make_root(self, node):
        self.root = node
        node.parent = None

    def left_rotate(self, node):
        #       1                           3
        #        \                         / \
        #         3         becomes       1   4
        #       /  \                       \
        #      2    4                       2

        old_parent = node

        # Right child becomes new parent
        # Right child becomes new root if old parent was root
        new_parent = old_parent.right_child
        if old_parent.is_root:
            self.make_root(new_parent)

        # Left child of new parent becomes right child of old parent
        old_parent.add_right_child(new_parent.left_child)

        # Old parent becomes left child of new parent
        new_parent.add_left_child(old_parent)
        return new_parent

    def right_rotate(self, node):
        #       4                           2
        #      /                           / \
        #     2           becomes         1   4
        #    / \                             /
        #   1   3                           3

        old_parent = node

        # Left child becomes new parent
        # Left child becomes new root if old node was root
        new_parent = old_parent.left_child
        if old_parent.is_root:
            self.make_root(new_parent)

        # Right child of new parent becomes left child of old parent
        old_parent.add_left_child(new_parent.right_child)

        # Old parent becomes right child of new parent
        new_parent.add_right_child(old_parent)
        return new_parent

    def left_right_rotation(self):
        #       1                        1                         2
        #        \       after            \        after          / \
        #         3      right             2       left          1   3
        #        /       rotation           \      rotation
        #       2                            3
        # Right rotate the right child of the root
        new_parent = self.right_rotate(self.root.right_child)

        # Add new parent as right child of root
        self.root.add_right_child(new_parent)

        # Left rotate the root
        self.left_rotate(self.root)

    def right_left_rotation(self):
        #        3                          3                     2
        #       /          after           /      after          / \
        #      1           left           2       right         1   3
        #      \          rotation      /        rotation
        #       2                      1
        # Left rotate the left child of the root
        new_parent = self.left_rotate(self.root.left_child)

        # Add new parent as left child of root
        self.root.add_left_child(new_parent)

        # Right rotate the root
        self.right_rotate(self.root)

    @property
    def tree_is_left_heavy(self):
        return self.root.balance_factor < 0 and self.height > 1

    @property
    def tree_is_right_heavy(self):
        return self.root.balance_factor > 0 and self.height > 1

    def rebalance(self):
        # If tree is left heavy and left child is right heavy
        if self.tree_is_left_heavy:
            if self.root.left_child.is_right_heavy:
                self.right_left_rotation()
            else:
                self.right_rotate(self.root)

        # If tree is right heavy and right child is left heavy
        if self.tree_is_right_heavy:
            if self.root.right_child.is_left_heavy:
                self.left_right_rotation()
            else:
                self.left_rotate(self.root)

    def get_parent(self, node):
        parent = self.root
        while True:
            if parent.left_child and node.value < parent.value:
                parent = parent.left_child
            elif parent.right_child and node.value >= parent.value:
                parent = parent.right_child
            else:
                return parent

    def add(self, value):
        node = Node(value)
        if self.is_empty:
            self.make_root(node)
        else:
            parent = self.get_parent(node)
            node.add_as_parent(parent)
        self.rebalance()
        self.nodes_added = set()
        self.save_nodes_as_list(self.root)

    def find(self, value):
        search_node = self.root
        while search_node and search_node.value != value:
            search_node = search_node.left_child if value < search_node.value else search_node.right_child
        return search_node

    def get_successor(self, node):
        # Left most node of the right child
        node = node.right_child
        while node.left_child:
            node = node.left_child
        return node

    def replace(self, node, successor):
        # Successor  =  Replacement node
        # Successor cannot have left child as it is the leftmost child
        # If successor has right child
        if successor.right_child:
            self.connect_right_child_to_parent(successor)

        # Disconnect node from parent
        node_parent = node.parent
        self.remove_parent_link(node)

        # Add old node's parent as successor's parent
        successor.add_as_parent(node_parent)

        # Add old node's left child as successor's left child
        successor.add_left_child(node.left_child)

        # If successor is not right child of old node
        # Add old node's right child as successor's right child
        if successor != node.right_child:
            successor.add_right_child(node.right_child)

        # If old node was root, make successor as the new root
        if node.is_root:
            self.make_root(successor)

    def remove(self, value):
        node_to_remove = self.find(value)
        if not node_to_remove:
            return 'Node not present'

        if node_to_remove.has_no_children:
            self.remove_parent_link(node_to_remove)
        elif node_to_remove.has_both_children:
            successor = self.get_successor(node_to_remove)
            self.replace(node_to_remove, successor)
        else:
            if node_to_remove.left_child:
                self.connect_left_child_to_parent(node_to_remove)
            else:
                self.connect_right_child_to_parent(node_to_remove)

        node_to_remove.parent = node_to_remove.left_child = node_to_remove.right_child = None
        self.rebalance()
        self.nodes_added = set()
        self.save_nodes_as_list(self.root)

    def pre_order_traversal(self, node):
        # Process the node, then left child and then right child
        # usefull for copying a tree
        if node:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def in_order_traversal(self, node):
        # Process the left child, then node and then right child
        # Use full for printing sorted tree
        if node:
            self.in_order_traversal(node.left_child)
            print(node.value, end=' ')
            self.in_order_traversal(node.right_child)

    def post_order_traversal(self, node):
        # Process the left child, then right child and then node
        # usefull in delete a node
        if node:
            self.post_order_traversal(node.left_child)
            self.post_order_traversal(node.right_child)
            print(node.value, end=' ')

    def get_position_to_insert(self, node):
        max_items_at_level = 2**node.height
        max_pos_at_level = 2*(node.height-1)+max_items_at_level
        parent_pos = self.nodes.index(node.parent)

        if len(self.nodes) < max_pos_at_level + 1:
            # First node on a new level
            for _ in range(max_items_at_level):
                self.nodes.append(None)

        return 2*parent_pos+1 if node.is_left_child_of_parent else 2*parent_pos+2

    def save_nodes_as_list(self, node):
        if node:
            if node not in self.nodes_added:
                if node.is_root:
                    self.nodes = [node]
                else:
                    node_pos = self.get_position_to_insert(node)
                    self.nodes[node_pos] = node

                self.nodes_added.add(node)
                self.save_nodes_as_list(node.left_child)
                self.save_nodes_as_list(node.right_child)

    def __str__(self):
        def nodes_at_height(height):
            def line(num):
                if num in (0, 2, 4):
                    return " " * start_gap + \
                        (" "*int(bw_gap)).join(['-'*NODE_LEN
                                                if node else " " * NODE_LEN
                                                for node in nodes])

                elif num == 1:
                    return " " * start_gap + \
                        (" "*int(bw_gap)).join([f'|{str(node).zfill(2):^11}|'
                                                if node else ' ' * NODE_LEN
                                                for node in nodes])

                else:
                    return " " * start_gap + \
                        (" "*int(bw_gap)).join([f'|Parent:{str(node.parent).zfill(2):^4}|'
                                                if node and node.parent
                                                else f'|Parent:None|'
                                                if node else ' ' * NODE_LEN
                                                for node in nodes])

            num_items = 2 ** height
            start_gap = 2**(max_height-height)*(justify) - \
                (justify) if height != max_height else 0
            bw_gap = (total_rec_len - (2*start_gap) -
                      (NODE_LEN*num_items))/(num_items-1) if height > 0 else 0
            min_pos = 2**height - 1
            max_pos = min_pos + num_items
            nodes = self.nodes[min_pos:max_pos]

            return '\n'.join([line(i) for i in range(5)])

        NODE_LEN = 13
        justify = NODE_LEN-NODE_LEN//2
        max_height = self.height
        num_items_at_max_height = 2 ** max_height
        total_rec_len = num_items_at_max_height * \
            NODE_LEN + (num_items_at_max_height-1)
        return '\n'.join([nodes_at_height(i) for i in range(max_height+1)])


if __name__ == '__main__':
    from random import randint
    from time import sleep
    tree = AVLTree()

    # Add random numbers to tree
    for _ in range(10):
        sleep(2)
        print('*'*20)
        num = randint(1, 99)
        print('\nAdding:', num)
        tree.add(num)
        print(tree)
