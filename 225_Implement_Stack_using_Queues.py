class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return False

    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return False

    def empty(self):
        return len(self.stack) == 0
        
        