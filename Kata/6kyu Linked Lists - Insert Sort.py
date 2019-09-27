"""Linked Lists - Insert Sort

Write an InsertSort() function which rearranges nodes in a linked list so they are sorted in increasing order. You can use the SortedInsert() function that you created in the "Linked Lists - Sorted Insert" kata below. The InsertSort() function takes the head of a linked list as an argument and must return the head of the linked list.

var list = 4 -> 3 -> 1 -> 2 -> null
insertSort(list) === 1 -> 2 -> 3 -> 4 -> null
If the passed in head node is null or a single node, return null or the single node, respectively. You can assume that the head node will always be either null, a single node, or a linked list consisting of multiple nodes.

"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new_node = Node(data)

    if not head:
        head = new_node
        return head

    node = head

    while node:

        if data < node.data:
            new_node.next = node
            return new_node

        if node.next is None:
            node.next = new_node
            return head

        if node.data <= data <= node.next.data:
            new_node.next = node.next
            node.next = new_node
            return head

        node = node.next


def insert_sort(head):

    if not head or head.next is None:
        return head

    new_head = None

    while head:
        new_head = sorted_insert(new_head, head.data)
        head = head.next

    return new_head
