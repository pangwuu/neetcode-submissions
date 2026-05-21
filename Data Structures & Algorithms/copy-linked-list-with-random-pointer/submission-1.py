"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        # first pass to make an map of old nodes -> new nodes
        cursor = head
        new_head = None

        # we instead map the OLD node to the new node
        mapping = {}

        while cursor is not None:
            new_val = cursor.val
            new_next = cursor.next
            new_random = cursor.random
            
            new_cursor = Node(new_val, new_next, new_random)

            if not new_head:
                new_head = new_cursor

            mapping[cursor] = new_cursor

            cursor = cursor.next
        
        second_pass_cursor = new_head
        while second_pass_cursor is not None:
            # replace the next and random (if its not none) with the mapped version
            if second_pass_cursor.next:
                second_pass_cursor.next = mapping[second_pass_cursor.next]
            if second_pass_cursor.random:
                second_pass_cursor.random =  mapping[second_pass_cursor.random]
            
            second_pass_cursor = second_pass_cursor.next
        
        return new_head
