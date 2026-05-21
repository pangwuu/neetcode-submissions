# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getSum(self, head: ListNode) -> int:
        # helper function to get the sum of a number in this dumbass format
        cursor = head
        totalSum = 0
        power = 0

        while cursor is not None:
            totalSum += cursor.val * (10 ** power)
            power += 1
            cursor = cursor.next
        
        return totalSum

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        intTotal = self.getSum(l1) + self.getSum(l2)
        string_format = str(intTotal)

        # a number like 12345 converts to 5 -> 4 -> 3 -> 2 -> 1 so we iterate through the string in the OTHER direction
        print(string_format)
        head = ListNode(int(string_format[-1]))
        cursor = head

        for i in range(len(string_format) - 2, -1, -1):
            new_node = ListNode(int(string_format[i]))
            cursor.next = new_node
            cursor = cursor.next
        
        return head