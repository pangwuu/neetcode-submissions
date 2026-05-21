class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        # ["1","2","+","3","*","4","-"] = 5
        # ["1","2","+","3","4","-", "*"] = -3

        stack = []

        for token in tokens:
            # if it's a number push it onto the stack
            print(token)
            # print(stack)

            if token not in "+-/*":
                # it is a number
                stack.append(token)
                print(stack)
                continue
            else:
                # if it's an operation - get the top two items on the stack,
                # and perform said operation with them

                # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

                last = int(stack.pop())
                second_last = int(stack.pop())

                print(f'Operation: {second_last} {token} {last}')

                if token == '+':
                    # add the top two numbers, push result onto stack
                    stack.append(last + second_last)
                elif token == '-':
                    stack.append(second_last - last)
                elif token == '*':
                    stack.append(last * second_last)                
                elif token == '/':
                    stack.append(int(second_last / last))

                print(stack)

        return int(stack[0])