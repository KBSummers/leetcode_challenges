#!usr/bin/env python

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

# If fast and slow start at same head, and we move
# fast twice as fast as slow, we can encounter the beginning of
# a cycle when the two nodes are equal.
# then since fast starts at head.next, we need to move slow one step forward

class Solution:
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head
