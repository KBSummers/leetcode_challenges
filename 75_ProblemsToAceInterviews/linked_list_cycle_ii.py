#!usr/bin/env python



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
