# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def checkEqualTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False
        
        return (root.val == subRoot.val and self.checkEqualTree(root.left, subRoot.left) and self.checkEqualTree(root.right, subRoot.right))

    def dfs(self, root, subRoot):
        if not root:
            return False
        else:
            result = self.checkEqualTree(root, subRoot)

            leftResult = self.dfs(root.left, subRoot)
            rightResult = self.dfs(root.right, subRoot)
            if (leftResult or rightResult) or result:
                return True

            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        