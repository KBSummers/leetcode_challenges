#!usr/bin/env python


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
