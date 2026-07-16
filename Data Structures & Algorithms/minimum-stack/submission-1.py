class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini[-1],val))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini.pop()
        else:
            return None
    def top(self) -> int:
        if len(self.stack) == 0:
            return -1 
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack)==0:
            return None
        else:
            return self.mini[-1]



        
        


        
