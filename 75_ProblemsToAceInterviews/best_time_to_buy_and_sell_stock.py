#!usr/bin/env python

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution:
    def maxProfit(self, prices):
        if prices == None or len(prices) == 0:
            return 0
        mn = prices[0]
        mx = 0
        for i in range(len(prices)):
            # we keep track of smallest
            # because anything after that larger
            # than current difference of prices
            # will result in more profit
            money = prices[i] - mn
            if money > mx:
                mx = money
            if prices[i] < mn:
                mn = prices[i]
        return mx
