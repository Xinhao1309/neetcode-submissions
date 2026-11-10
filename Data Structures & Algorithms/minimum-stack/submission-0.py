class MinStack:

    def __init__(self):
        self.size = 0
        self.original_stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.original_stack.append(val)

        if self.size <= 0 or val < self.min_stack[self.size -1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[self.size -1])
        self.size += 1   

    def pop(self) -> None:
        self.original_stack.pop()
        self.min_stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.original_stack[self.size - 1]

    def getMin(self) -> int:
        return self.min_stack[self.size - 1]
