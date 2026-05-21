from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Input: s = "OUZODYXAZV", t = "XYZ"
        # Input: s = "YXAAAAAAAAAAAAAAAAAAAYZXYZ", t = "XYZ"

        if len(t) > len(s):
            return ""
        
        if len(t) == len(s):
            t_count = Counter(t)
            s_count = Counter(s)
            if t_count == s_count:
                return s
            return ""

        t_count = Counter(t)
        best = s
        
        found = False
        # find the first substring which has at least t_count
        current_counts = Counter()
        
        l = 0
        print(f'T count={t_count}')
        for r, char in enumerate(s):

            if char in current_counts:
                current_counts[char] += 1
            else:
                current_counts[char] = 1

            # is this not an O(m) check each time - unique in
            while current_counts >= t_count:
                found = True
                print(f'l={l}, r={r}')
                print(f'Current counts={current_counts}')
                

                # valid! We now simply need to optimise this
                # solution to the best we can do

                # O(k) to make a copy
                curr_best = s[l:r + 1]
                if len(curr_best) < len(best):
                    best = curr_best

                current_counts[s[l]] -= 1
                l += 1
        
        if not found:
            return ""

        return best
            


        


