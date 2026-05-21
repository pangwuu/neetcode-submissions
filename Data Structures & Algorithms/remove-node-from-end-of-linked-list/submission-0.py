# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # special cases: start, end or middle

        # get length
        cursor = head
        length = 0
        while cursor is not None:
            cursor = cursor.next
            length += 1
        
        # get number of steps to move forward 
        forward_steps = length - n

        # special case
        if forward_steps == 0:
            return head.next
        
        before_removed = head
        for _ in range(forward_steps - 1):
            before_removed = before_removed.next
        
        before_removed.next = before_removed.next.next
        return head
        if before_removed.next.next is None:
            # that means we're removing the last element
            before_removed.next = None
            return head
        




        