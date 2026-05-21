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
        queue = deque([(root, 0)])

        while queue:
            node = queue.popleft()
            node_val = node[0].val
            node_level = node[1]

            bfs_traversal.append((node[0], node_level))
            if node[0].left:
                queue.append((node[0].left, node_level + 1))
            if node[0].right:
                queue.append((node[0].right, node_level + 1))
        
        print([(node[0].val, node[1]) for node in bfs_traversal])
        
        # make empty lists corresponding to each level (the level of the last node is by definition the lowest)
        levels = []
        current_level = 0

        for node in bfs_traversal:
            value = node[0]
            depth = node[1]
            if depth >= current_level:
                # add a new level
                levels.append([])
                current_level += 1
            
            levels[-1].append(value.val)

        return levels



            