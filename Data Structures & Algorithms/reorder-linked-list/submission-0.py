# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printListPretty(self, head) -> None:
        if not head:
            print("No List")
            return
        while head:
            print(f'{head.val} -> ', end='')
            head = head.next
        print()
        return

    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the 2nd half of the list - then restich
        # get length
        length = 0
        cursor = head
        while cursor is not None:
            cursor = cursor.next
            length += 1
        
        # going forward "half" times is the last node in the stiched array
        half = length // 2

        end_of_first = head
        for _ in range(half - 1):
            end_of_first = end_of_first.next
        
        beginning_of_second = end_of_first.next

        # split the two lists
        end_of_first.next = None
        
        # now we can reverse this 2nd linked list 
        prev = None
        curr = beginning_of_second
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # do two traversals to test em
        self.printListPretty(head)
        self.printListPretty(prev)

        # now we stitch them together
        add_list_1 = False
        list_1_ptr = head.next
        list_2_ptr = prev # prev is now the new head of the 2nd linked list
        
        while list_1_ptr or list_2_ptr:
            if list_1_ptr is None:
                add_list_1 = False
                
            if add_list_1:
                head.next = list_1_ptr
                list_1_ptr = list_1_ptr.next
            else:
                head.next = list_2_ptr
                list_2_ptr = list_2_ptr.next
            
            head = head.next

            add_list_1 = not add_list_1

