# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthHelper(self, root, curr_depth):
        if root is None:
            return curr_depth
        else:
            curr_depth += 1
            return max(self.maxDepthHelper(root.left, curr_depth), self.maxDepthHelper(root.right, curr_depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)