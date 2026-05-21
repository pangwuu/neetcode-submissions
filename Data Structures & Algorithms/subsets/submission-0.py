class Solution:
    def subsetsHelper(self, nums: List[int], currentSubsets: List[List[int]], unique: Set[Tuple[int]]):
        # you have two choices, add this number, or not
        if len(nums) == 0:
            # no more things to add. Return the current subsets
            return currentSubsets
        
        added = nums[0]
        
        # for each set, we duplicate it - and with the copy we add "added"
        for i in range(len(currentSubsets)):
            subset = currentSubsets[i]
            newSubset = subset[:]
            newSubset.append(added)
            newUniqueTuple = tuple(newSubset)
            # ensure we dont have duplicates
            if newUniqueTuple in unique:
                continue
            
            unique.add(newUniqueTuple)
            currentSubsets.append(newSubset)
        
        return self.subsetsHelper(nums[1:], currentSubsets, unique)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        empty_set = []

        all_subsets.append(empty_set)
        unique = set()
        unique.add(())

        return self.subsetsHelper(nums, all_subsets, unique)