__author__ = 'James'


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        "Push an item to the end of the stack."
        self.items.append(item)

    def pop(self):
        "Pop the last item from the stack and return it."
        if not self.is_empty(): return self.items.pop()
        else: return None

    def peek(self):
        "Get the value of the top element in the stack.":w
        return None if self.is_empty() else self.items[-1]
