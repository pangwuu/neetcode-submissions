# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        queue = deque([root])

        if root is None:
            return []

        while queue:
            current_level_length = len(queue)
            current_level = []
            for _ in range(current_level_length):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)      
            levels.append(current_level)

        return [level[-1].val for level in levels]
        