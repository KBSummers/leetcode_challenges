#!usr/bin/env python

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""

class Solution:
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1: return n
        # we will tail all the way down until we reach 0 and 1,
        # then it will keep returning all the way to n-1 + n-2
        return self.fib(n-1) + self.fib(n-2)
