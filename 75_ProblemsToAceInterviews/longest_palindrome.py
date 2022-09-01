#!usr/bin/env python
"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
class Solution:
    def longestPalindrome(self, s):
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is number of odd letters
        # so we return number of even letters plus 1
        if len(hash) > 0:
            return len(s) - len(hash) + 1
        else:
            return len(s)
