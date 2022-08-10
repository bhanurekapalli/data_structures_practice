class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return
        nodeStack = []
        nodeStack.append(root)
        list_post_order = []
        out_list = []
        while len(nodeStack) > 0:
            curr = nodeStack.pop()
            out_list.append(curr.val)
            if curr.left is not None:
                nodeStack.append(curr.left)
            if curr.right is not None:
                nodeStack.append(curr.right)
        while len(out_list) > 0:
            list_post_order.append(out_list.pop())

        return list_post_order


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(6)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(Solution().postorderTraversal(root))
