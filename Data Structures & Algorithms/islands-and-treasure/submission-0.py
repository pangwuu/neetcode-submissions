from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(treasureChestLocationX: int, treasureChestLocationY: int) -> None:
            '''
            Fills each findable land cell with the distance from this treasure chest, or keeps the current value
            if there is a closer treasure chest.
            '''
            nonlocal grid

            # queue stores (x, y) pairs
            queue = deque([(treasureChestLocationX, treasureChestLocationY)])
            visited = set()
            distanceFromChest = 0

            while queue:
                for _ in range(len(queue)):
                    print(f'running: queue = {queue}')
                    
                    # pop and process
                    cell = queue.popleft()
                    print(cell)

                    # check if it's actually land
                    if cell in visited:
                        continue

                    x = cell[0]
                    y = cell[1]
                    visited.add(cell)
                    
                    # inacessible bounds
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
                        continue

                    cell_value = grid[x][y]
                    print(cell_value)
                    
                    if cell_value == -1:
                        continue
                    
                    if cell_value == 0 and x != treasureChestLocationX and y != treasureChestLocationY:
                        # any treasures that aren't the original
                        continue     

                    # check if this cell doesn't have a closer treasure chest
                    if distanceFromChest < cell_value:
                        print(f'writing {distanceFromChest}')
                        grid[x][y] = distanceFromChest

                    # add all neighbours – don't even worry about bounds checks
                    queue.append((x + 1, y))
                    queue.append((x - 1, y))
                    queue.append((x, y + 1))
                    queue.append((x, y - 1))
                
                distanceFromChest += 1
        
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                if grid[row_index][column_index] == 0:
                    bfs(row_index, column_index)
