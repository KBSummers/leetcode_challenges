#!usr/bin/env python
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums, target):
        return self.bsearch(nums, target, 0, len(nums)-1)
    #recursive
    def bsearch(self, nums, target, low, high):
        if low > high:
            return -1
        mid = (low + high) / 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.bsearch(nums, target, mid + 1, high)
        else:
            return self.bsearch(nums, target, low, mid - 1)

####################################

    # lazy version
    def search(self, nums, taget):
        try:
            return nums.index(target)
        except:
            return -1
