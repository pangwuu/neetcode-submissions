class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        # starts = "([{"
        ends = "}])"
        for char in s:
            if char in matches:
                # push onto stack
                stack.append(char)
            elif char in ends:
                # see if the last thing on the stack matches
                if not stack:
                    return False

                if matches[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False