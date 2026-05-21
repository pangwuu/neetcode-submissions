class Solution:
    def findMin(self, nums: List[int]) -> int:
            left = 0
            right = len(nums) - 1

            # one side is sorted, one side is not sorted
            # and we return the element when we see that mid - 1 > mid!

            while left <= right:
                # compare mid and right

                mid = (left + right) // 2

                if nums[mid] < nums[right]:
                    # the right side is sorted! - we should go to the left side
                    right = mid
                else:
                    left = mid + 1
                
            return nums[left - 1]
                
