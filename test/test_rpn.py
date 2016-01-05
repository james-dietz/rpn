__author__ = 'James'
from rpn import RPN

def test_RPN_evaluate():
    inst = RPN()
    s = "12 7 * 18 + 47 8 / - 3 +"
    assert inst.evaluate(s) == [99.125]

def test_RPN_stack_underflow():
    inst = RPN()
    s = "1 +"
    assert inst.evaluate(s) == "Stack underflow"