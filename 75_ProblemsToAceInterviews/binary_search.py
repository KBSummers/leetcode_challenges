#!usr/bin/env python

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
