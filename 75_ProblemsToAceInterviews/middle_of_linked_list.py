#!/usr/bin/env python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Idea:
# traverse with two nodes, one twice as fast,
# then return the 1/2 fast one when faster one
# reaches the end
class Solution:
    def middleNode(self, head):
        half = last = head
        # check for both to cover
        # even and odd number of node
        while last and last.next:
            half = half.next
            last = last.next.next
        return half
