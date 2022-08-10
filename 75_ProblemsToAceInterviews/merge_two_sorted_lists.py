#! usr/bin/env python

class Solution:

    # Using recursion
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val < b.val:
                a, b = b, a
            a.next = mergeTwoLists(a.next, b)
        return a or b

    # iteratively
    def mergeTwoLists(self, a, b):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                cur.next = list2
                list2, curr = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next
