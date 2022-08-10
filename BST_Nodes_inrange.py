class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        if root is None:
            return
        current = root
        stack = []  # initialize stack
        inorder_list=[]
        while True:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)

                current = current.left

                # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif (stack):
                current = stack.pop()
                inorder_list.append(current.val)
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break
        return inorder_list

    def solve(self,A,B,C):
        inorder_list = self.inorderTraversal(A)
        count=0
        for x in inorder_list:
            if x >=B and x<=C:
                count=count+1
        return count

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right=TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    inorder_list=Solution().inorderTraversal(root)
