class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = set()
        
        def backtrack(index: int, currentCombination: List[int]):
            # choose, explore, check validity, repeat
            nonlocal combs, nums, target

            # is the current a valid solution?
            if currentCombination:
                s = sum(currentCombination)
            else:
                currentCombination = []
                s = 0
            
            if s == target:
                sorted_comb = tuple(sorted(currentCombination))
                if sorted_comb not in combs:
                    combs.add(sorted_comb)
                
                sorted_comb = []
                return
            
            elif index >= len(nums):
                return

            elif s > target:
                # this is now invalid. Remove the last number – and try again
                # undo it
                # if currentCombination:
                #     currentCombination.pop()
                
                return # Just stop exploring this option
            
            # you should have an option where you 
            # a) take this number again.
            currentCombination.append(nums[index])
            backtrack(index, currentCombination)

            # b) don't take said number – increment the index
            if currentCombination:
                currentCombination.pop()
            backtrack(index + 1, currentCombination)
        
        backtrack(0, [])

        return list([list(comb) for comb in combs])