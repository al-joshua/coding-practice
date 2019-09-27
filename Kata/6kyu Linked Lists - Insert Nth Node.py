"""Linked Lists - Insert Nth

Implement an InsertNth() function (insert_nth() in PHP) which can insert a new node at any index within a list.

InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below.
Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that
it has the given index. InsertNth() should return the head of the list.

insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)
You must throw/raise an exception (ArgumentOutOfRangeException in C#, InvalidArgumentException in PHP)
if the index is too large.

The push() and buildOneTwoThree() (build_one_two_three() in PHP) functions do not need to be redefined.
The Node class is also preloaded for you in PHP."""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_nth(head, index, data):
    new_node = Node(data)
    i = 0
    if index == 0:
        new_node.next = head
        return new_node

    node = head

    while node:
        if i == index - 1:
            new_node.next = node.next
            node.next = new_node
            return head
        node = node.next
        i += 1

    raise IndexError
