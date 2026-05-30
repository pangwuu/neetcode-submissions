class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapper = {}
        for index, num in enumerate(nums):
            # get new position
            mapper[num] = (index + k) % len(nums)

        for num, position in mapper.items():
            nums[position] = num
