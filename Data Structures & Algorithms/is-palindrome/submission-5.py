class Solution:
    def isPalindrome(self, s: str) -> bool:

        # new_s_list = []

        # s_list = [i for i in s]

        # for letter in s_list:
        #     # filter out
        #     if letter.isalpha() or letter.isnumeric():
        #         new_s_list.append(letter)
        
        # new_s = "".join(new_s_list).lower().strip()
        # print(new_s)

        # for index in range(len(new_s) // 2):
        #     if new_s[index] != new_s[-index - 1]:
        #         return False

        # return True

        l_ptr = 0
        r_ptr = len(s) - 1

        s = s.lower().strip()
        while l_ptr < r_ptr:
            # Move them until they're alphabetical or numeric
            l = s[l_ptr]
            while not l.isalpha() and not l.isnumeric() and l_ptr < r_ptr:
                l_ptr += 1
                l = s[l_ptr]

            r = s[r_ptr]
            while not r.isalpha() and not r.isnumeric() and l_ptr < r_ptr:
                r_ptr -= 1
                r = s[r_ptr]                
            
            if l != r:
                return False
            
            l_ptr += 1
            r_ptr -= 1
        
        return True


