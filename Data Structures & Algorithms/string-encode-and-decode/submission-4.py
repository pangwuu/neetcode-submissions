delimiter = '#'
class Solution:

    def encode(self, strs: List[str]) -> str:
        # when seeing a new string, encode with length of the string followed by delimiter
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append(delimiter)
            encoded.append(s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # upon seeing a number, read FROM the delimiter
        decoded = []
        index = 0
        while index < len(s):
            # read a number until delimiter
            num_start = index
            while s[index] != '#':
                index += 1
            # extract number of characters to read - O(1) time as the substring is max 3 chars
            number = int(s[num_start:index])

            # skip over the #
            index += 1

            # add the substring
            decoded.append(s[index:index + number]) # also O(1) time as each string is max 200

            index += number
        
        return decoded