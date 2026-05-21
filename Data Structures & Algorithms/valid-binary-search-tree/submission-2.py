# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTHelper(self, root, currMax, currMin):
        # having currMax and currMin allow us to track previous nodes


        # a tree is valid if it's subtrees are valid
        if not root:
            return True
        if root.left and root.right:
            if root.left.val >= root.val or root.right.val <= root.val or root.left.val >= currMax or root.right.val <= currMin:
                return False
        if root.left:
            if root.left.val >= root.val or root.left.val >= currMax:
                return False
        if root.right:
            if root.right.val <= root.val or root.right.val <= currMin:
                return False
        if root.val >= currMax or root.val <= currMin:
            return False
            
        return self.isValidBSTHelper(root.left, root.val, currMin) and self.isValidBSTHelper(root.right, currMax, root.val) 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('inf'), float('-inf'))
