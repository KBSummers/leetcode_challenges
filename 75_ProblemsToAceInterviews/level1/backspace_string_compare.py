#!/usr/bin/env python

"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""
class Solution:
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def back(res, c):
            if c != '#' : res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, s, []) == reduce(back, t, [])
