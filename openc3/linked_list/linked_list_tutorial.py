"""
Linked List Tutorial
-------------------
A linked list is a sequence of nodes where each node contains a value and a reference to the next node.
This file demonstrates how to create and manipulate a singly linked list in Python.

Composition:
This implementation uses composition, where the LinkedList class is composed of Node objects.
Each Node instance holds data and a reference to the next Node, and the LinkedList manages these nodes to provide
list operations. Composition allows for flexible and modular design, making it easy to extend or
modify linked list behavior.

Operations covered:
- Traversal
- Insertion (at head, tail, and after a given node)
- Deletion (by value)
- Search
- Update

Example usage is provided at the end.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        """Print all values in the list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def insert_at_head(self, value):
        """
        Insert a new node at the beginning.
        Composition is here
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node at the end."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_value, value):
        """Insert a new node after the node with prev_value."""
        current = self.head
        while current and current.value != prev_value:
            current = current.next
        if current:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def delete_by_value(self, value):
        """Delete the first node with the given value."""
        current = self.head
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if not current:
            return  # Value not found
        if not prev:
            self.head = current.next  # Delete head
        else:
            prev.next = current.next

    def search(self, value):
        """Return True if value is found, else False."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def update(self, old_value, new_value):
        """Update the first node with old_value to new_value."""
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return True
            current = current.next
        return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.traverse()  # 1 -> 2 -> 3 -> None
    ll.insert_at_tail(4)
    ll.traverse()  # 1 -> 2 -> 3 -> 4 -> None
    ll.insert_after(2, 2.5)
    ll.traverse()  # 1 -> 2 -> 2.5 -> 3 -> 4 -> None
    ll.delete_by_value(3)
    ll.traverse()  # 1 -> 2 -> 2.5 -> 4 -> None
    print(ll.search(2.5))  # True
    ll.update(2.5, 5)
    ll.traverse()  # 1 -> 2 -> 5 -> 4 -> None
