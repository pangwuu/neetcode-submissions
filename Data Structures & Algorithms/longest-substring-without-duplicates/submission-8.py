class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 0
        l = 0
        in_string = set()

        for r, char in enumerate(s):
            
            while char in in_string:
                in_string.remove(s[l])
                l += 1
            
            in_string.add(char)
            max_len = max(max_len, r - l + 1)
            
        return max_len
            


                