
def sort_by_first(n):
    return n[1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        num_freq_list = list(counts.items())
        intermediate = sorted(num_freq_list, key=sort_by_first, reverse=True)
        return [y[0] for y in intermediate][:k]

        