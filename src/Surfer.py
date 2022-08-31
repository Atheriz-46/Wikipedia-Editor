class Surfer:
    stack = []

    def currentTop(self):
        if len(self.stack) == 0:
            return "HomePage.md"
        else:
            return self.stack[-1]
    
    def back(self):
        if len(self.stack) > 0:
            self.stack.pop()
        return self.currentTop()
    
    def push(self,x):
        self.stack.append(x)

