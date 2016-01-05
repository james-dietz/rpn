__author__ = 'James'
from stack import Stack

def test_stack_is_empty():
    inst = Stack()
    assert inst.is_empty()

def test_stack_not_empty():
    inst = Stack()
    inst.push(1)
    assert not inst.is_empty()

def test_stack_empty_pop():
    inst = Stack()
    assert inst.pop() == None

def test_stack_pop():
    inst = Stack()
    inst.push(1)
    assert inst.pop() == 1

def test_stack_empty_peek():
    inst = Stack()
    assert inst.peek() == None

def test_stack_peek():
    inst = Stack()
    inst.push(1)
    assert inst.peek() == 1 and not inst.is_empty()