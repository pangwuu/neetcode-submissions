from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort an individual string
        returned = []
        anagram_to_index = {} # points a specific sorted string to its index in returned

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagram_to_index:
                returned[anagram_to_index[sorted_s]].append(s)
            else:
                anagram_to_index[sorted_s] = len(returned)
                returned.append([s])
        
        return returned

