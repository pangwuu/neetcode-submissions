class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if abs(right - left) < 3:
                # just linear search in O(1) time
                segment = nums[left: right + 1]
                if target in segment:
                    return segment.index(target) + left
                return -1

            # which side is sorted?
            leftSorted = True
            if nums[right] > nums[middle]:
                leftSorted = False

            if leftSorted:
                # is the target in the sorted side?
                if nums[left] < target and target < nums[middle]:
                    # search in the left
                    right = middle
                    continue
                # search in the right
                left = middle + 1
            elif not leftSorted:
                # is the target in the sorted side? - the sorted side is the RIGHT
                if nums[middle] < target and target < nums[right]:
                    left = middle + 1
                    continue
                right = middle
        
        return -1


