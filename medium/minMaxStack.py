class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.max = []
        self.min = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.max.pop()
        self.min.pop()
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
        self._pushMin(number)
        self._pushMax(number)

    def _pushMin(self, number):
        minimum = self.min[-1] if len(self.min) > 0 else float("inf")
        self.min.append(min(minimum, number))

    def _pushMax(self, number):
        maximum = self.max[-1] if len(self.max) > 0 else float("-inf")
        self.max.append(max(maximum, number))

    def getMin(self):
        return self.min[-1]

    def getMax(self):
       return self.max[-1]
