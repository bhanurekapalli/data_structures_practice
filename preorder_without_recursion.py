# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return
        nodeStack = []
        nodeStack.append(root)
        list_pre_order = []
        while len(nodeStack) > 0:
            curr = nodeStack.pop()
            list_pre_order.append(curr.val)
            if curr.right is not None:
                nodeStack.append(curr.right)
            if curr.left is not None:
                nodeStack.append(curr.left)
        return list_pre_order


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    print(Solution().preorderTraversal(root))
