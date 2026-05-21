class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0] * len(temperatures)

        stack = [] # (index, temp)

        # loop from the back with a monotonic decreasing stack

        for i in range(len(temperatures) - 1, -1, -1):
            
            temp = temperatures[i]
            print(i, temp, stack)

            # pop off all elements on the stack that are less than than temp
            while stack and stack[-1][1] <= temp:
                stack.pop()
            
            if stack:
                # the next highest would be top element on the stack (monotonic decreasing)
                next_highest = stack[-1]
                results[i] = next_highest[0] - i
            else:
                results[i] = 0
            
            stack.append((i, temp))
        
        return results
