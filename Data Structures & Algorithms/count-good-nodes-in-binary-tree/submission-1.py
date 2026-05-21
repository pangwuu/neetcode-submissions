# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesHelper(self, root, currentMax, goodNodes):
        if not root:
            return goodNodes
        else:
            # two cases, either it's a good node or not
            if root.val >= currentMax:
                # YAY good node
                currentMax = root.val
                goodNodes.add(root)
                
            # run on left and right
            return self.goodNodesHelper(root.left, currentMax, goodNodes) | self.goodNodesHelper(root.right, currentMax, goodNodes)

    def goodNodes(self, root: TreeNode) -> int:
        return len(self.goodNodesHelper(root, root.val, set()))
        