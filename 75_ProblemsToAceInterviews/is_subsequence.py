#!usr/bin/env python

class Solution:
    def isSubsequence(self, s, t):
        i = j = 0
        # increment j every loop and i only if it equals that
        # jth index in the other word
        # if i is the length of that substring at the end
        # we have a substring
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j +=1
        return i == len(s)
