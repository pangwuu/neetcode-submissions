class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1

        while left_ptr < right_ptr:
            curr_sum = numbers[left_ptr] + numbers[right_ptr]
            if curr_sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif curr_sum < target:
                left_ptr += 1
            elif curr_sum > target:
                right_ptr -= 1

        return [0, 0]        