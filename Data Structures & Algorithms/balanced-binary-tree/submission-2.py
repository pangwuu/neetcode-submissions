# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedHelper(self, root, height):
        if not root:
            return (height, True)
        else:
            leftResult = self.isBalancedHelper(root.left, height)
            rightResult = self.isBalancedHelper(root.right, height)
            
            height = max(leftResult[0], rightResult[0]) + 1

            if abs(leftResult[0] - rightResult[0]) > 1 or not leftResult[1] or not rightResult[1]:
                return (height, False)
            return (height, True)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # the tree is balanced if the left subtree is balanced, and the right subtree is balanced
        return self.isBalancedHelper(root, 1)[1]