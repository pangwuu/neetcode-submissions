class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        currentSubset = []

        def backtrack(index: int):
            nonlocal result
            nonlocal currentSubset

            if index >= len(nums):
                result.append(currentSubset.copy())
                return 
            
            # include
            currentSubset.append(nums[index])
            backtrack(index + 1)

            # don't include - need to pop it first!
            currentSubset.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return result

             