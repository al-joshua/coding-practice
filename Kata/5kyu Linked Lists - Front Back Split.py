"""Linked Lists - Front Back Split

Write a FrontBackSplit() function that takes one list and splits it into two sublists — one for the front half,
and one for the back half. If the number of elements is odd, the extra element should go in the front list.
For example, FrontBackSplit() on the list 2 -> 3 -> 5 -> 7 -> 11 -> null
should yield the two lists 2 -> 3 -> 5 -> null and 7 -> 11 -> null.
Getting this right for all the cases is harder than it looks.
You will probably need special case code to deal with lists of length < 2 cases.

var source = 1 -> 3 -> 7 -> 8 -> 11 -> 12 -> 14 -> null
var front = new Node()
var back = new Node()
frontBackSplit(source, front, back)
front === 1 -> 3 -> 7 -> 8 -> null
back === 11 -> 12 -> 14 -> null
You should throw an error if any of the arguments to FrontBackSplit are null or if the source list has < 2 nodes.

Hint. Probably the simplest strategy is to compute the length of the list, then use a for loop to hop over
the right number of nodes to find the last node of the front half, and then cut the list at that point.
There is a trick technique that uses two pointers to traverse the list. A "slow" pointer advances one nodes
at a time, while the "fast" pointer goes two nodes at a time. When the fast pointer reaches the end,
the slow pointer will be about half way. For either strategy, care is required to split the list at the right point."""


import Linked_Lists as ll


""" For your information:"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def front_back_split(source, front, back):
    if bool(source and front and back) == False:
        raise Exception('Incorrect input')

    if source.data is None or source.next is None:
        raise Exception('Source is 0 or 1 nodes')

    if source.next.next is None:
        front.data = source.data
        back.data = source.next.data

    else:
        curr_slow = curr_fast = source

        while curr_fast.next and curr_fast.next.next:
            curr_slow = curr_slow.next
            curr_fast = curr_fast.next.next

        back.data, back.next = curr_slow.next.data, curr_slow.next.next
        curr_slow.next = None
        front.data, front.next = source.data, source.next