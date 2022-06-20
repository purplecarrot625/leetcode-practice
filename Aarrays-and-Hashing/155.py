class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # each minimum value at this point, so we don't need worry about the pop out values(compare to the case which store the minimum value as a single variable)
    def push(self, val: int) -> None:
        self.stack.append(val)
        value = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()