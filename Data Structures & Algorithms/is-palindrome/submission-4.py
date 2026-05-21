class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s_list = []

        s_list = [i for i in s]

        for letter in s_list:
            # filter out
            if letter.isalpha() or letter.isnumeric():
                new_s_list.append(letter)
        
        new_s = "".join(new_s_list).lower().strip()
        print(new_s)

        for index in range(len(new_s) // 2):
            if new_s[index] != new_s[-index - 1]:
                return False

        return True

