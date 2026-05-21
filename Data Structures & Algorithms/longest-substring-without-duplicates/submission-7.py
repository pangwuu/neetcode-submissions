class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 1
        l_ptr = 0
        r_ptr = 0

        while r_ptr < len(s):
            
            # check if this new substring is valid
            r_ptr += 1
            substring = s[l_ptr:r_ptr]
            if len(set(substring)) == r_ptr - l_ptr:
                
                # valid! add to it if needed
                longest = max(r_ptr - l_ptr, longest)
                
            else:
                
                # invalid - move l_ptr until the substring becomes valid
                while len(set(s[l_ptr:r_ptr])) != r_ptr - l_ptr:
                    l_ptr += 1  
                
                
            
        return longest
            


                