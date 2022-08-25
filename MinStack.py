class MinStack(object):
    def __init__(self):
        self.min = None
        self.stack = []
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
    def getMin(self):
        return self.min
