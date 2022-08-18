#!usr/bin/env python
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
