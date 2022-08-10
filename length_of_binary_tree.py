# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, node):
        if node is None:
            return 0

        else:
            lDepth = self.solve(node.left)
            rDepth = self.solve(node.right)

        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1
