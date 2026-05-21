# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root, currentHeight):
        if not root:
            return 0
        else:
            height = max(self.maxHeight(root.left, currentHeight), self.maxHeight(root.right, currentHeight)) + 1
            # make a new field for the max height of every node?
            root.maxHeight = height
            return height
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we traverse - at each stage, we see
        if not root:
            return 0

        self.maxHeight(root, 0)

        maxDiameter = 0
        stack = [root]
        while stack:
            # pop the node off of the stack
            node = stack.pop()
            print(f'node value: {node.val}, maxheight: {node.maxHeight}')

            # so the max diameter = max height of left + max height of right
            if node.left and node.right:
                currDiameter = node.left.maxHeight + node.right.maxHeight
            elif node.left:
                currDiameter = node.left.maxHeight
            elif node.right:
                currDiameter = node.right.maxHeight
            else:
                currDiameter = maxDiameter

            maxDiameter = max(currDiameter, maxDiameter)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        
        return maxDiameter

