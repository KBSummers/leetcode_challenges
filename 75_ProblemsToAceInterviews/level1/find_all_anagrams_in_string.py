#!usr/bin/env python3

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# sliding window technique

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        for ch in p: hm[ch] += 1

        for i in range(pL - 1):
            if s[i] in hm: hm[s[i]] -= 1

        for i in range(-1, sL - pL + 1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i + pL < sL and s[i + pL] in hm:
                hm[s[i + pL]] -= 1

            if all(v == 0 for v in hm.values()):
                res.append(i + 1)
        return res
