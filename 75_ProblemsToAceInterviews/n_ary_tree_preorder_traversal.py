#!usr/bin/env python

"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""
class Solution:
    def preorder(self, root):
        output = []
        self.traverse(root, output)
        return output

    def traverse(self, node, output):
        if not node:
            return
        output.append(node.val)
        for child in node.children:
            self.traverse(child, output)
