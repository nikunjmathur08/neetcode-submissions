class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            curr_min = min(val, self.getMin())
            tup = (val, curr_min)
            self.stack.append(tup)
        else:
            tup = (val, val)
            self.stack.append(tup)

    def pop(self) -> None:
        popped = self.stack.pop()
        return popped[0]

    def top(self) -> int:
        last = self.stack[-1]
        return last[0]

    def getMin(self) -> int:
        return self.stack[-1][1]

