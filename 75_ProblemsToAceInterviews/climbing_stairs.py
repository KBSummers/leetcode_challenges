#!usr/bin/env python
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
# This problem can be solved with the use of the Fibonacci Sequence.
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
