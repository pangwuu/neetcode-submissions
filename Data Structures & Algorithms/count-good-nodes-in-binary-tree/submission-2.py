# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currentMax):
            if not root:
                return 0
            
            total = 0
            if root.val >= currentMax:
                currentMax = root.val
                total += 1
            
            total += dfs(root.left, currentMax)
            total += dfs(root.right, currentMax)
            return total
        
        return dfs(root, float('-inf'))
        
            