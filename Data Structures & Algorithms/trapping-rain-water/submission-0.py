class Solution:
    def trap(self, height: List[int]) -> int:
        # max at a specific position = min(max of left, max of right) - height

        # get the max of any number to the left 
        index_to_lmax = {}
        index_to_lmax[0] = -1
        current_lmax = -1
        for index, num in enumerate(height):
            if num > current_lmax:
                current_lmax = num
            index_to_lmax[index] = current_lmax
        
        # do the same but to the right
        index_to_rmax = {}
        current_rmax = -1
        for index in range(len(height) -1, -1, -1):
            num = height[index]
            if num > current_rmax:
                current_rmax = num
            index_to_rmax[index] = current_rmax
        
        print(index_to_lmax)
        print(index_to_rmax)

        total_water = 0
        for index, _ in enumerate(height):
            water_at_point = max(min(index_to_lmax[index], index_to_rmax[index]) - height[index], 0)
            total_water += water_at_point
        
        return total_water

        

