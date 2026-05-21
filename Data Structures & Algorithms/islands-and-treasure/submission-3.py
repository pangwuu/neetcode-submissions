from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # get the location of all treasures
        treasureCoords = deque([])
        for row_index, row in enumerate(grid):
            for column_index, val in enumerate(row):
                if val == 0:
                    treasureCoords.append((row_index, column_index))
        
        # now we do BFS
        distance = 0
        visited = set()

        while treasureCoords:
            for _ in range(len(treasureCoords)):

                coord = treasureCoords.popleft()
                x = coord[0]
                y = coord[1]

                if grid[x][y] > distance:
                    grid[x][y] = distance

                # get all valid neighbours
                movements = [
                    [0, 1],
                    [1, 0],
                    [0, -1],
                    [-1, 0]
                ]

                for movement in movements:
                    newX = x + movement[0]
                    newY = y + movement[1]
                    if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[newX]):
                        if (newX, newY) not in visited \
                        and grid[newX][newY] != -1 \
                        and grid[newX][newY] != 0:
                            # then valid - add the new coord
                            treasureCoords.append((newX, newY))
                            visited.add((newX, newY))
            
            distance += 1
