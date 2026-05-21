"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # map the OLD node to a new node
        mapping = {}

        def dfs(startNode: Optional['Node']):
            '''
            performs a DFS. 
            Result is a mapping of all old nodes to new ones
            '''
            nonlocal mapping

            if not startNode or not startNode.neighbors:
                return
            if startNode in mapping:
                return
            
            newNode = Node(startNode.val)
            mapping[startNode] = newNode

            for oldNode in startNode.neighbors:
                if oldNode not in mapping:
                    dfs(oldNode)
        
        # get the mapping
        dfs(node)

        # now we perform DFS again, but we recreate the links with the newly created nodes
        def secondDFS(startNode: Optional['Node']):
            nonlocal mapping
            
            if not startNode:
                return
            
            oldNode = startNode

            if oldNode not in mapping:
                return

            newNode = mapping[oldNode]

            for oldNeighbour in oldNode.neighbors:
                newNeighbour = mapping[oldNeighbour]
                if newNeighbour not in newNode.neighbors:
                    newNode.neighbors.append(newNeighbour)
                    secondDFS(oldNeighbour)
        
        secondDFS(node)
                    
        if node not in mapping:
            return Node(node.val)
        
        return mapping[node]


            