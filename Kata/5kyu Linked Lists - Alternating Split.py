"""Linked Lists - Alternating Split

Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists.
The sublists should be made from alternating elements in the original list. So if the original
list is a -> b -> a -> b -> a -> null then one sublist should be a -> a -> a -> null and
the other should be b -> b -> null.

###JavaScript

var list = 1 -> 2 -> 3 -> 4 -> 5 -> null
alternatingSplit(list).first === 1 -> 3 -> 5 -> null
alternatingSplit(list).second === 2 -> 4 -> null
###Python

list = 1 -> 2 -> 3 -> 4 -> 5 -> None
alternating_split(list).first == 1 -> 3 -> 5 -> None
alternating_split(list).second == 2 -> 4 -> None
###Ruby


list = 1 -> 2 -> 3 -> 4 -> 5 -> nil
alternating_split(list).first == 1 -> 3 -> 5 -> nil
alternating_split(list).second == 2 -> 4 -> nil
For simplicity, we use a Context object to store and return the state of the two linked lists.
A Context object containing the two mutated lists should be returned by AlternatingSplit().

If the passed in head node is null/None/nil or a single node, throw an error."""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    first_curr = first = Node(head.data)
    second_curr = second = Node(head.next.data)
    i = 1

    while head.next:
        if i % 2:
            if head.next.next:
                first_curr.next = Node(head.next.next.data)
                first_curr = first_curr.next
            else:
                first_curr.next = None
        else:
            if head.next.next:
                second_curr.next = Node(head.next.next.data)
                second_curr = second_curr.next
            else:
                second_curr.next = None

        head = head.next
        i += 1

    return Context(first, second)