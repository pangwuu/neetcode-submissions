from collections import defaultdict

class Solution:
    def getFreqDict(self, s: str) -> dict:
        freqs = defaultdict(int)

        for char in s:
            freqs[char] += 1
        
        return freqs

    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = self.getFreqDict(s1)
        
        for index, char in enumerate(s2):
            if char in f1 and index + len(s1) <= len(s2):
                potential_str = s2[index: index + len(s1)]
                potential_permute = self.getFreqDict(potential_str)
                if f1 == potential_permute:
                    return True
        
        return False


