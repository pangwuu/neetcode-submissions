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
        curr = root

        while stack or curr:
            # go as far left as possible (this is our smallest value)
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # now we can go up by 1
            curr = stack.pop()
            k -= 1

            # if k was 1, then it means smallest value. k = number of times we need to go right
            if k == 0:
                return curr.val
            curr = curr.right
            

        return inorder_traversal[k - 1].val