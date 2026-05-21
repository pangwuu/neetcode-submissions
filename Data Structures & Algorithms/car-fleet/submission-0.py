class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [4,1,0,7], speed = [2,2,1,1]

        # [(7, 1), (4, 2), (1, 1), (0, 1)]

        combined = [(position[i], speed[i]) for i in range(len(position))]
        
        # Consist of tuples of (position, speed) in descending order of position
        combined_sorted = sorted(combined, key=lambda x: x[0], reverse=True)

        fleets = 0
        new_fleet = True
        time = -1

        for car in combined_sorted:
            position = car[0]
            speed = car[1]
            if new_fleet:
                # calculate time needed to travel
                time = (target - position) / speed
                fleets += 1
                new_fleet = False
            else:
                # see if this car can reach the first one in the fleet 
                # (i.e. the current value of time) before the target.
                projected = time * speed + position

                # if it cannot, start a new fleet and increase fleet count by 1
                if projected < target:
                    time = (target - position) / speed
                    fleets += 1
            
        return fleets
                    

                