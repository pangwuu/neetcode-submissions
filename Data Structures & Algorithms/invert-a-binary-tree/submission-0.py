# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        tmp = root.right
        root.right = root.left
        root.left = tmp
        return root 





        if not root:
            return None

        if not root.left and not root.right:
            # no children
            return root
        elif root.left:
            # no right child
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
            return root
        elif root.right:
            # no left child
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root