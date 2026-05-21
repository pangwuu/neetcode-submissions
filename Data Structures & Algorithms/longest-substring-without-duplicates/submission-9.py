class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        chars = set()
        longest = 0

        while right < len(s):
            # make it 1 larger and update longest if needed
            if s[right] not in chars:
                chars.add(s[right])
                longest = max(len(chars), longest)
                right += 1
                continue
            else:
                # shift the left pointer and remove elements from
                # the set UNTIL there are no repeating characters
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
        
        return longest


            
                    
                
                