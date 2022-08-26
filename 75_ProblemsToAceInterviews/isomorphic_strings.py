#!usr/bin/env python

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
# Checking to see if letters in 's' can be translated to other
# letters in 't' to form the word
#
# Example:
# s = "egg", t = "foo"   --> True
# s = "foo", t - "bar"   --> False
class Solution:
    def isIsomorphic(self, s, t):
        if len(t) != len(s):
            return False
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            # we log the translations..
            # if, on any pass, the translation doesn't match
            # after this, we just return false.
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
