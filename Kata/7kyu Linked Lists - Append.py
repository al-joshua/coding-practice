"""Linked Lists - Append

Write an Append() function which appends one linked list to another. The head of the resulting list should be returned.

var listA = 1 -> 2 -> 3 -> null
var listB = 4 -> 5 -> 6 -> null
append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
If both listA and listB are null/NULL/None/nil, return null/NULL/None/nil.
If one list is null/NULL/None/nil and the other is not, simply return the non-null/NULL/None/nil list."""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA, listB):
    if not listA and not listB:
        return None

    if not listA or not listB:
        return listA or listB

    curr = listA

    while curr.next:
        curr = curr.next

    curr.next = listB

    return listA
