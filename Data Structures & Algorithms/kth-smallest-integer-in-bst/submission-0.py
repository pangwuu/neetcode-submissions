# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # get the size of the tree first
        
        stack = [root]
        def dfs(root, traversal):
            if not root:
                return traversal
            else:
                dfs(root.left, traversal)
                traversal.append(root)
                dfs(root.right, traversal)
                
                return traversal
        
        inorder_traversal = dfs(root, [])
        # print([node.val for node in inorder_traversal])

        # dfs_traversal = []

        # while stack:
        #     node = stack.pop()
            
        #     if node.right:
        #         stack.append(node.right)            
        #     dfs_traversal.append(node)
        #     if node.left:
        #         stack.append(node.left)    

        # nums = [node.val for node in dfs_traversal]   
        # print(nums)
        
        return inorder_traversal[k - 1].val