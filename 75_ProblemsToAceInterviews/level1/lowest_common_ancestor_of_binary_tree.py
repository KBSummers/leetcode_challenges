#!usr/bin/env python

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        # if both left and right returned,
        # p and q have been found, so parent is LCA
        if left and right:
            return root
        # Either p or q has been found on the left or right branch
        # meaning the other one is somewhere below where its counterpart
        # has been found, so we dont need to search more, just return
        # node where we found p or q at
        else:
            return left or right
