class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operators = ["+", "-", "*", "/"]

        running_total = 0

        first_time = True

        for token in tokens:
            if token in operators:
                # pop 2 elements, and eval them
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                
                if token == "+":
                    stack.append(int(num_1 + num_2))
                elif token == "-":
                    stack.append(int(num_1 - num_2))
                elif token == "*":
                    stack.append(int(num_1 * num_2))
                elif token == "/":
                    stack.append(int(num_1 / num_2))                                                            

            else:
                # push number onto the stack
                stack.append(int(token))
        
        return stack[-1]


