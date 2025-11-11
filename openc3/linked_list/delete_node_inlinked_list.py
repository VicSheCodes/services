"""
There is a singly-linked list head and we want to delete a node node in it.
You are given the node to be deleted node. You will not be given access to the first node of head.
All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
Delete the given node.

Note that by deleting the node, we do not mean removing it from memory. We mean:
The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.

Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.


Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
"""

class ListNode:
 def __init__(self, x):
     self.value = x
     self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head

        while current:
            print(current.value, end="->")
            current = current.next

        # empty LinkedList
        print("None")

    def insert_at_head(self, value):
        # create new ListNode
        new_node = ListNode(value)

        # update new node next to pint on the head
        new_node.next = self.head

        # update the head to point on the new_node
        self.head = new_node

    def delete_by_value(self, value):
        current = self.head
        prev = None

        while current and current.value != value:
            # proceed to the next node
            prev = current
            current = current.next

        # value not fount
        if not current:
            print(f"Value {value} not fount.")
            return

        # delete the head
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next

head = [4,5,1,9]
node = 5

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.value = node.next.value
            node.next = node.next.next

def build_linked_list(values):
    pass


def find_node(head, value):
    pass


def traverse(head):
    pass
