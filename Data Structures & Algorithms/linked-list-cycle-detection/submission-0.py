# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        # general idea: a fast and slow pointer. If the fast catches to the slow ever - there is a cycle
        fast = head
        slow = head

        while fast is not None and slow is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
        
        return False
