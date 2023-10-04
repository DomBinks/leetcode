class MinStack:

    def __init__(self):
        # Tops of the start are at the end of the list
        self.stack = [] # Normal stack
        self.minStack = [] # Stack of minimal values

    def push(self, val: int) -> None:
        self.stack.append(val) # Add to the normal stack

        # If this value is the current minimum or a new minimum
        if self.minStack == [] or (self.minStack != [] and val <= self.minStack[-1]):
            self.minStack.append(val) # Add it to the minimum stack

    def pop(self) -> None:
        # If the top of the stack is equal to the top of the minimum stack
        if self.stack[-1] == self.minStack[-1]:
            # Remove the top of the minimum stack as this value is being removed
            self.minStack = self.minStack[:-1]

        self.stack = self.stack[:-1] # Remove the top of the stack

    def top(self) -> int:
        # Get the top of the normal stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Get the top of the minimum stack
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
