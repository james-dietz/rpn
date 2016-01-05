__author__ = 'James'
from stack import Stack
import operator


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
        output = self.stack.items if not error else "Stack underflow"
        self.stack.items = []
        return output

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
