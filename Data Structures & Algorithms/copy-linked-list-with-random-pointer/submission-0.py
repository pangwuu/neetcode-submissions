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

        # first pass to make an array of copied nodes
        cursor = head
        new_nodes = []

        # allows us to see which memory address 
        lookup = {}

        i = 0

        while cursor is not None:
            # make new node
            new_val = cursor.val
            next_ptr = cursor.next
            # random remains None for now
            new_node = Node(new_val, next_ptr)
            new_nodes.append(new_node)

            lookup[cursor] = i
            i += 1
            cursor = cursor.next
        
        for node_index in range(len(new_nodes) - 1):
            new_nodes[node_index].next = new_nodes[node_index + 1]

        random_pass_cursor = head
        i = 0

        while random_pass_cursor is not None:
            # find where the old node points to, and change said node in new_nodes to fit that

            if random_pass_cursor.random is not None:
                random_ptr_position = lookup[random_pass_cursor.random]
                print(f"changing {random_pass_cursor.val}'s index: {random_ptr_position}")
                new_nodes[i].random = new_nodes[random_ptr_position]

            i += 1
            random_pass_cursor = random_pass_cursor.next
    
        return new_nodes[0]

