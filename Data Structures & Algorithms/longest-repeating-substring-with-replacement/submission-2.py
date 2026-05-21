from collections import defaultdict

class Solution:

    def bruteForce(self, s: str, k: int) -> int:
        
        max_len = 0
        for index, char in enumerate(s):
            # try to greedily replace k letters
            first_char = char
            curr_len = 0
            while k >- 0 and index < len(s):
                if s[index] != first_char:
                    k -= 1
                curr_len += 1
                index += 1

            max_len = max(curr_len, max_len)
        return max_len
            
    def characterReplacement(self, s: str, k: int) -> int:
        # Testcase: AAABAAABBBBBBBBBBBBABBBBBBB, k = 2

        visited_freq = {}

        l = 0
        max_len = 0
        for r, char in enumerate(s):
            # check if it is valid - use the values of the dictionary
            if char in visited_freq:
                visited_freq[char] += 1
            else:
                visited_freq[char] = 1

            vals = visited_freq.values()
            allowed_swaps = sum(vals) - max(vals)

            while allowed_swaps > k:
                # remove the old left
                visited_freq[s[l]] -= 1
                l += 1
                
                # check if valid again
                vals = visited_freq.values()
                allowed_swaps = sum(vals) - max(vals)
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
            
            



















