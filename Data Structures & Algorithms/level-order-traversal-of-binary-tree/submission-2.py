# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        bfs_traversal = []
        queue = deque([root])

        while queue:
            # the number of nodes in this level is the number currently in the queue
            processed_number = len(queue)
            bfs_traversal.append([])
            for _ in range(processed_number):
                node = queue.popleft()
                bfs_traversal[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return bfs_traversal



            