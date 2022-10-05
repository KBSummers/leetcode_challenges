#!usr/bin/env python

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        cfreq = {}
        maxStringLen = 0
        for r in range(len(s)):
            if not s[r] in cfreq:
                cfreq[s[r]] = 0
            cfreq[s[r]] += 1

            cellCount = r - l + 1
            if cellCount - max(cfreq.values()) <= k:
                maxStringLen = max(maxStringLen, cellCount)
            else:
                cfreq[s[l]] -= 1
                if not cfreq[s[l]]:
                    cfreq.pop(s[l])
                l += 1
        return maxStringLen
