# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def binarySearch(self, root, node, traversal):
        # search for root, and return the traversal
        if not root:
            return traversal
        else:
            traversal.append(root)
            if root.val == node.val:
                return traversal
            
            # add this to the path taken down
            if node.val < root.val:
                return self.binarySearch(root.left, node, traversal)
            elif node.val > root.val:
                return self.binarySearch(root.right, node, traversal)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.binarySearch(root, p, [])
        q_path = self.binarySearch(root, q, [])
        
        best = root
        print(p_path, q_path)
        for p_node, q_node in zip(p_path, q_path):
            print(p_node.val, q_node.val)
            
            if p_node.val == q_node.val:
                best = p_node

        return best