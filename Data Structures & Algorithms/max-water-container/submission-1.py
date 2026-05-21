class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(heights) - 1
        max_water = 0

        while l_ptr < r_ptr:
            # calculate water
            curr_water = min(heights[l_ptr], heights[r_ptr]) * (r_ptr - l_ptr)
            if curr_water > max_water:
                max_water = curr_water
            
            if heights[l_ptr] < heights[r_ptr]:
                l_ptr += 1
            else:
                r_ptr -= 1
        
        return max_water