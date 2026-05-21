class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.extra == []:
            # empty stack
            self.extra.append(val)
        else:
            self.extra.append(min(val, self.extra[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extra[-1]

