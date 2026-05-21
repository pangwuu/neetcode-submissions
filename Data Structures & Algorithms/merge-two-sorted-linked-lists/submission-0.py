# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        p1 = list1
        p2 = list2

        sorted_list_ptr = ListNode(min(p1.val, p2.val))
        head = sorted_list_ptr
        
        if p1.val < p2.val:
            p1 = p1.next
        else:
            p2 = p2.next

        # at each step, compare then iterate if needed
        while p1 and p2:
            if p1.val > p2.val:
                sorted_list_ptr.next = ListNode(p2.val)
                p2 = p2.next
            else:
                sorted_list_ptr.next = ListNode(p1.val)
                p1 = p1.next
            sorted_list_ptr = sorted_list_ptr.next
        
        # if not same length, add the rest of the other one
        while p1:
            sorted_list_ptr.next = ListNode(p1.val)
            p1 = p1.next
            sorted_list_ptr = sorted_list_ptr.next

        while p2:
            sorted_list_ptr.next = ListNode(p2.val)
            p2 = p2.next
            sorted_list_ptr = sorted_list_ptr.next
        
        return head


