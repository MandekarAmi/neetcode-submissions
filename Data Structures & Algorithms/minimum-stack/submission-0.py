class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if isinstance(val, int):
            self.stack.append(val)
        else:
            self.stack.append(None)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
