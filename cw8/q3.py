class CustomStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return f"CustomStack({self.stack})"
    
    def __repr__(self):
        return f"CAustomStack({self.stack})"

stack = CustomStack()
print(stack)
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
print(len(stack)) # Output: 3
print(repr(stack)) # Output: CustomStack([1, 2, 3])
print(str(stack)) # Output: CustomStack([1, 2, 3])
print(stack.pop()) # Output: 3
print(stack) # Output: CustomStack([1, 2])