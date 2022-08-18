#!usr/bin/env python

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
