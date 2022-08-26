#! usr/bin/env python3
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
class Solution:

    # Using recursion
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val < b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

    # iteratively
    def mergeTwoLists(self, a, b):
        cur = dummy = ListNode()
        while a and b:
            if a.val < b.val:
                curr.next = a
                a, curr = a.next, a
            else:
                cur.next = b
                b, curr = b.next, b

        if a or b:
            cur.next = a if a else b
        return dummy.next
