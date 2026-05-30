class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot_sources = []
        for x, row in enumerate(grid):
            for y, fruit_num in enumerate(row):
                if fruit_num == 2:
                    rot_sources.append((x, y))
        
        time = 0

        while rot_sources:
            # at each step, mark all adjacent fruits
            adjacent_fruits = set()
            for source in rot_sources:
                # check all directions and mark if it's a 1
                movements = (
                    (0, 1), 
                    (0, -1), 
                    (-1, 0), 
                    (1, 0)
                )
                for movement in movements:
                    new_source = (source[0] + movement[0], source[1] + movement[1])
                    # bounds check
                    if new_source[0] < 0 or new_source[0] >= len(grid) or new_source[1] < 0 or new_source[1] >= len(grid[0]):
                        continue
                    
                    # check if it is indeed a fresh fruit
                    if grid[new_source[0]][new_source[1]] == 1:
                        adjacent_fruits.add(new_source)
                
            # make all sources 0 to avoid resurrecting fruits
            for source in rot_sources:
                grid[source[0]][source[1]] = 0

            # make all adjacent fruits rotten
            for fruit in adjacent_fruits:
                grid[fruit[0]][fruit[1]] = 2

            # And your next set of rot sources
            rot_sources = list(adjacent_fruits)
            time += 1
        
        # check if there's any remaining fresh fruits
        for x, row in enumerate(grid):
            for y, fruit_num in enumerate(row):
                if fruit_num == 1:
                    return -1
        

        return max(time - 1, 0)
            