class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min = None
        self.max = None
        self.peekElement = None
        self.prevMinValues = []
        self.prevMaxValues = []

    def min(self):
        if self.min:
            return self.min
        return None

    def max(self):
        if self.max:
            return self.max
        return None

    def peek(self):
        return self.peekElement

    def push(self, value):
        if len(self.stack) == 0:
            self.min = value
            self.max = value
            self.stack.append(value)
        else:
            self.min = min(self.min, value)
            self.max = max(self.max, value)
            self.stack.append(value)
        self.prevMinValues.append(self.min)
        self.prevMaxValues.append(self.max)
        self.peekElement = self.stack[-1]

    def pop(self): # challenge implemeting it in constant time
        if len(self.stack) >= 1:
            removedValue = self.stack.pop()
            self.prevMinValues.pop()
            self.prevMaxValues.pop()
            prevMinValue = self.prevMinValues[-1]
            prevMaxValue = self.prevMaxValues[-1]
            self.peekElement = self.stack[-1]
            self.min = prevMinValue
            self.max = prevMaxValue




stack = MinMaxStack()
stack.push(5)
print(stack.min, stack.max, stack.peekElement)
stack.push(7)
print(stack.min, stack.max, stack.peekElement)
stack.push(2)
print(stack.min, stack.max, stack.peekElement)
stack.pop()
print(stack.min, stack.max, stack.peekElement)
stack.pop()
print(stack.min, stack.max, stack.peekElement)