#!usr/bin/env python

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution:
    def runningSum(nums):
        total = 0
        results = []
        for num in nums:
            total += num
            results.append(total)
        return results
