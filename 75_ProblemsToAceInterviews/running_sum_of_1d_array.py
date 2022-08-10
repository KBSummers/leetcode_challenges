#!usr/bin/env python

class Solution:
    def runningSum(nums):
        total = 0
        results = []
        for num in nums:
            total += num
            results.append(total)
        return results
