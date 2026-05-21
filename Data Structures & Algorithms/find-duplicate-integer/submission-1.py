class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # just fast/slow pointer?
        fast = 0
        slow = 0

        while True:
            # move twice for fast
            fast = nums[fast]
            fast = nums[fast]

            slow = nums[slow]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow