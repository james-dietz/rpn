__author__ = 'James'


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # Push an item to the end of the stack.
    def push(self, item):
        self.items.append(item)

    # Pop the last item from the stack and return it.
    def pop(self):
        if not self.is_empty(): return self.items.pop()
        else: return None

    # Get the value of the top element in the stack.
    def peek(self):
        return None if self.is_empty() else self.items[-1]
