__author__ = 'James'
import operator


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


class RPN:
    def __init__(self):
        self.stack = Stack()
        # Data in format op: (fn, number of input args)
        self.operators = {"+": (operator.add, 2),
                          "-": (operator.sub, 2),
                          "*": (operator.mul, 2),
                          "/": (operator.truediv, 2)
                         }

    def evaluate(self, input_string):
        # Initialise error flag
        error = False
        # Tokens delimited by spaces
        for substr in input_string.split(" "):
            # Test if token is a number
            try:
                f = float(substr)
            except ValueError:
                # If not, check if it is an operator
                if substr in self.operators.keys():
                    # Handle all operators immediately
                    try:
                        self.handle_op(substr)
                    # If the stack underflows, break out of the loop
                    except IndexError:
                        # Set error flag to true and break
                        error = True
                        break
                # Drop all malformed input silently
                else:
                    continue
            else:
                # Push number casted to float
                self.stack.push(f)
        if not error:
            print(",".join([str(e) for e in self.stack.items]))
        else:
            print("Stack underflow")
        self.stack.items = []


    def handle_op(self, op):
        data = self.operators[op]
        fn = data[0]
        args = []
        # Get args from stack.
        # Number of args popped is found in data[1]
        for i in range(data[1]):
            # Attempt to pop an item from the stack
            token = self.stack.pop()
            # Stack.pop() returns None if the stack is empty
            if token is None:
                raise IndexError
            else:
                args.append(token)
        # Cast to tuple, needed to pass to function
        args = tuple(args)[::-1]
        try:
            out = {fn(*args)}
        # Catch all exceptions
        except Exception as e:
            print("{} in {}({})".format(type(e), fn, args))
        else:
            # Push all outputs to stack
            [self.stack.push(i) for i in out]
