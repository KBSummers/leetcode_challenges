#!usr/bin/env python

class Solution:
    def pivotIndex(nums):
        left = 0
        right = sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
