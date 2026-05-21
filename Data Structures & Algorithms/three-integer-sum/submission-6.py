from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(f'sorted numbers: {sorted_nums}')
        triplets = []

        seen_triplets_indicies = set()
        seen_triplets = set()

        # new idea, do 2Sum (sorted version) for each value in the list

        for k, target_num in enumerate(sorted_nums):
            
            # so we are looking for sorted_nums[i] + sorted_nums[j] = -target_num
            real_target_num = -target_num
            print(f'k is {k}, negative target number is {real_target_num}')

            i = 0
            j = len(sorted_nums) - 1

            while i < j:

                print(i, j, k)
                print(f'{sorted_nums[i]} + {sorted_nums[j]} = {sorted_nums[i] + sorted_nums[j]} ')

                if i == k:
                    i += 1
                    continue
                if j == k:
                    j -= 1
                    continue

                if sorted_nums[i] + sorted_nums[j] < real_target_num:
                    # make it bigger
                    i += 1
                elif sorted_nums[i] + sorted_nums[j] > real_target_num:
                    j -= 1
                else:
                    adding = [sorted_nums[i], sorted_nums[j], target_num]

                    added_indicies = [i, j, k]

                    if not i != j != k:
                        if i == k:
                            i += 1
                        if j == k:
                            j -= 1
                        continue

                    # # prevent duplicates
                    # adding_tuple = tuple(sorted(added_indicies))
                    # if adding_tuple in seen_triplets_indicies:
                    #     i += 1
                    #     j -= 1  
                    #     continue       

                    triplet_hashable = tuple(sorted(adding))
                    if triplet_hashable in seen_triplets:
                        i += 1
                        j -= 1
                        continue

                    seen_triplets.add(triplet_hashable)               

                    # this is a triplet!
                    triplets.append(adding)
                    
                    print(f'Adding {adding} with distinct triplet {triplet_hashable}')

                    # missing something here?
                    i += 1
                    j -= 1
      
        return triplets
