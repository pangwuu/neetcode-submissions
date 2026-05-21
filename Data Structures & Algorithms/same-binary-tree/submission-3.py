# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def bfs(self, root):
        if not root:
            return None
        
        queue = deque([root])
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)

            if not node:
                continue

            queue.append(node.left)
            queue.append(node.right)
        
        return traversal


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        traversal1 = self.bfs(p)
        traversal2 = self.bfs(q)
        
        if traversal1 is None and traversal2 is None:
            return True
        
        if not traversal1 or not traversal2:
            return False
        if len(traversal1) != len(traversal2):
            return False

        for i, j in zip(traversal1, traversal2):
            if i is None and j is None:
                continue
            elif i is None and j != None:
                return False
            elif j is None and i != None:
                return False
            elif i.val != j.val:
                return False
        
        return True

        return self.bfs(p) == self.bfs(q)

        