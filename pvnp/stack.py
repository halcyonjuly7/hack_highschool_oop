class Stack:
    def __init__(self):
        self._stack = []
        self._size = 0

    def isEmpty(self):
        return not self._stack

    def push(self, data):
        self._stack.append(data)
        self._size += 1
    
    def pop(self):
        if self._size != 0:
           self._size -= 1 
           return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def __str__(self):
        return self._stack

