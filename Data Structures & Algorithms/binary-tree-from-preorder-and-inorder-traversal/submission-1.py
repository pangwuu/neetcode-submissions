# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def constructSubtree(root, inorderArray, preOrderArray):
            # constructs left and right subtrees given an inorder array
            if len(inorderArray) == 0:
                return None
            if len(inorderArray) == 1:
                return TreeNode(inorderArray[0])
            
            root = TreeNode(preOrderArray[0])
            root_index = inorderArray.index(preOrderArray[0])

            root.left = constructSubtree(root.left, inorderArray[:root_index], preOrderArray[1:root_index + 1])
            root.right = constructSubtree(root.right, inorderArray[root_index + 1:], preOrderArray[root_index + 1:])
            
            return root

        if not preorder and not inorder:
            return None
        
        # initialise a root
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        root.left = constructSubtree(root.left, inorder[:root_index], preorder[1:root_index + 1])
        root.right = constructSubtree(root.right, inorder[root_index + 1:], preorder[root_index + 1:])
        
        return root


        
