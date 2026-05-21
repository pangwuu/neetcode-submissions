from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # figure out the correct row
        row_l = 0
        row_r = len(matrix) - 1
        found_row_index = None

        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            # looking for one where matrix[row_m] < target and matrix[row_m + 1] > target
            
            if row_m == len(matrix) - 1: # bounds check
                found_row_index = row_m
                break
            elif matrix[row_m][0] <= target and matrix[row_m + 1][0] > target:
                found_row_index = row_m
                break

            elif matrix[row_m][0] < target:
                # remove bottom half of matrix
                row_l = row_m + 1
            elif matrix[row_m][0] > target:
                # remove top half
                row_r = row_m - 1
            
            
        if found_row_index is None:
            return False
        
        row = matrix[found_row_index]

        # do a binary search inside the row
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1

        return False
                