#!/usr/bin/env python3

COUNTER = 0
def iota(reset=False):
    
    global COUNTER
    if reset == True:
        COUNTER = 0
    result = COUNTER
    COUNTER += 1 
    return result 


OP_PUSH = iota()
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
OP_COUNT = iota()


def push(x):
    return (OP_PUSH, x)
def plus():
    return (OP_PLUS, )
def dump():
    return (OP_DUMP, )
def minus():
    return (OP_MINUS, )



def simulate(program):
    stack = []
    for op in program:
        assert OP_COUNT == 4, "exhustive usage of ops"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0]==OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif op[0]==OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            print("unreachble")


program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(3),
    push(1),
    minus(),
    dump(),
    ]






if __name__ == "__main__":
    simulate(program=program)
    