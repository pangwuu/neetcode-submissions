# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        left = None
        middle = head
        right = middle.next

        return_l = False
        return_m = False
        return_r = False

        while True:

            middle.next = left

            if right is None:
                return_m = True
                break

            left = right.next

            right.next = middle
            if left is None:
                return_r = True
                break            

            middle = left.next

            left.next = right
            if middle is None:
                return_l = True
                break            
            right = middle.next
        
        if return_l:
            return left
        elif return_m:
            return middle
        elif return_r:
            return right
