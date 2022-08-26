#!usr/bin/env python
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
# Recurrance relation:
# minCost(i) = cost[i] + min(minCost(i-1), minCost(i-2))
# Base Cases:
# minCost(0) = cost[0]
# minCost(1) = cost[1]
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        first = cost[0]
        second = cost[1]
        rest = cost[2:]
        if n <= 2: return min(first, second)
        for price in rest:
            curr = price + min(first, second)
            first = second
            second = curr
        return min(first, second)
