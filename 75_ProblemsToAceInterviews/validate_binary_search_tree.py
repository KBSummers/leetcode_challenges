#!usr/bin/env python

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, float("-inf"), float("inf"))

    def validate(self, node, lt, gt):
        if not node:
            return True
        if not lt < node.val < gt:
            return False
        # recursively check for left values less than current node
        # and that right values are greater than current node
        return (self.validate(node.left, lt, node.val) and self.validate(node.right, node.val, gt))
