from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def exploreIslandBFS(start: List[int]):
            
            '''
            starting from a given coordinate [x, y], explore the 
            whole island and return all coodinates of said island
            '''

            nonlocal grid

            movements = [
                [0, 1],
                [1, 0],
                [0, -1],
                [-1, 0]
            ]

            
            queue = deque([start])
            grid[start[0]][start[1]] = 0

            # this will track all cells so we don't double count
            size = 0

            while queue:
                cell = queue.popleft()
                size += 1

                # try to add any neighbours that are 1's (that are within bounds)
                for movement in movements:
                    newX = cell[0] + movement[0]
                    newY = cell[1] + movement[1]
                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]):
                        # bounds check okay
                        if grid[newX][newY] == 1:
                            # add this to queue
                            queue.append([newX, newY])
                            grid[newX][newY] = 0 # easier to not double count
            
            return size
        
        max_size = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    max_size = max(exploreIslandBFS([x, y]), max_size)
        
        return max_size

                    



        