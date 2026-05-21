class Solution:
    def explore(self, grid: List[List[str]], start: Tuple[int], currentIsland: Set[Tuple[int]]):
        '''
        Given an index pair, explore the island around this until we cannot anymore. This is essentially a DFS
        '''

        movements = [
            (-1, 0), 
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        
        x = start[0]
        y = start[1]
        
        # bound check

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return currentIsland
        
        # explore yourself
        if grid[x][y] == '1' and (x, y) not in currentIsland:
            currentIsland.add((x, y))
            grid[x][y] = '0'
        elif grid[x][y] == '0':
            # no need to explore it
            return currentIsland
        elif (x, y) in currentIsland:
            return currentIsland

        # explore all your neighbours
        for movement in movements:
            currentIsland = self.explore(grid, [x + movement[0], y + movement[1]], currentIsland)

        # return the island chain
        return currentIsland

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = set()
        islandChains = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x, y) not in islands:
                    # explore it
                    islandChains += 1
                    islandChain = self.explore(grid, [x, y], set())
                    
                    # we get back a set of tuples - union this with the total islands
                    islands = islands.union(islandChain)
        
        return islandChains


        