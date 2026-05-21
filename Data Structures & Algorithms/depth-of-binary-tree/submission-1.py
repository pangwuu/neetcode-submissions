# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        stack = [(root, 1)]
        maxDepth = 0

        while stack:
            # pop element
            popped = stack.pop()

            prev_node = popped[0]
            prev_depth = popped[1]
            
            maxDepth = max(maxDepth, prev_depth)

            # push any children
            if prev_node.left:
                stack.append((prev_node.left, prev_depth + 1))
            if prev_node.right:
                stack.append((prev_node.right, prev_depth + 1))
        
        return maxDepth
            