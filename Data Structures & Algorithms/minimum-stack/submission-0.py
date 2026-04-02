class MinStack:

    def __init__(self):
        self.items=[]
        

    def push(self, val: int) -> None:
        self.items.append(val)
        

    def pop(self) -> None:
        return self.items.pop()
        

    def top(self) -> int:
        return self.items[-1] if len(self.items) > 0 else None

        

    def getMin(self) -> int:
        return min(self.items)
        
