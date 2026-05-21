from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(board: List[List[int]], pacific=True):
            # returns a list of all coordinates that you
            # can reach from an ocean tile
            

            movements = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            # get coordinates of the first row and column
            ocean_tiles = []

            if pacific:
                ocean_tiles = [(i, 0) for i in range(len(heights))]
                ocean_tiles += [(0, i) for i in range(len(heights[0]))]
            elif not pacific:
                row_length_index = len(heights[0]) - 1
                ocean_tiles = [(i, row_length_index) for i in range(len(heights))]
                ocean_tiles += [(len(heights) - 1, i) for i in range(len(heights[0]))]
            
            # ocean_tiles = list(set(ocean_tilx/es))

            
            reachable = set()

            for ocean_tile in ocean_tiles:
                # we run a bfs here from this tile, ignoring any marked tiles
                queue = deque([ocean_tile])

                while queue:
                    coord = queue.popleft()
                    x = coord[0]
                    y = coord[1]

                    if (x, y) in reachable:
                        continue
                    
                    reachable.add((x, y))
                    
                    # try to go to other tiles in bounds
                    for movement in movements:
                        newX = x + movement[0]
                        newY = y + movement[1]
                        if newX >= 0 and newY >= 0 and newX < len(board) and newY < len(board[0]):
                            # works – check if it's not a hash
                            if (newX, newY) not in reachable and board[newX][newY] >= board[x][y]:
                                queue.append((newX, newY))
                
            return reachable
        
        
        pacific = bfs(heights)
        atlantic = bfs(heights, False)
        
        return list(pacific.intersection(atlantic))
