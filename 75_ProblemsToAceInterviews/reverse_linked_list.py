#!/usr/bin/env python3
"""
Given the head of a singly linked list, reverse the list, and return the reversed list
"""
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
