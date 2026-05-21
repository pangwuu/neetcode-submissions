
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use a hashmap to model the graph

        graph = {}
        for i in range(n):
            graph[i] = set()
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        connected_components = 0
        
        def dfs(startingEdge: List[int]) -> None:
            nonlocal graph

            stack = startingEdge

            while stack:
                visited_node = stack.pop()
                
                
                # look at its neighbours
                if visited_node not in graph:
                    continue
                
                neighbours = graph[visited_node]
                for neighbour in neighbours:
                    
                    graph[neighbour].remove(visited_node)
                    stack.append(neighbour)
                
                graph.pop(visited_node)


        for edge in edges:
            # run a dfs on this edge and remove all nodes within this component – 
            # but only increment if we havent' seen this before
            if edge[0] in graph or edge[1] in graph:
                dfs(edge)
                connected_components += 1
        
        return connected_components + len(graph)
            

