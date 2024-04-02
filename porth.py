#!/usr/bin/env python3

import sys


iota_counter = 0


def iota(reset=False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter = iota_counter + 1
    return result


OP_PUSH = iota(True)
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()


def push(x):
    return (OP_PUSH, x)


def plus():
    return (OP_PLUS,)


def minus():
    return (OP_MINUS,)


def dump():
    return (OP_DUMP,)


def simulate_program(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 4, "EXHAUSTIVE HANDLING OF SIMULATE PROGRAM"
        if (op[0] == OP_PUSH):
            stack.append(op[1])
        elif (op[0] == OP_PLUS):
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif (op[0] == OP_MINUS):
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif (op[0] == OP_DUMP):
            a = stack.pop()
            print(a)
        else:
            assert False, "unreachable"


def compile(program):
    assert False, "NOT implemented!"


program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(30),
    push(4),
    minus(),
    dump()
]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage{sys.argv[0]} <SUBCOMMAND> [ARGS]")
        print(f"SUBCOMMANDS:")
        print("     sim        simulate the program ")
        print("      com      compile the program ")
        print("ERROR: no subcommand provided")
        exit(-1)
    subcommand = sys.argv[1]
    if subcommand == "sim":
        simulate_program(program=program)
    elif subcommand == "com":
        print("Not implemented")
    else:
        print(f"UNKNOWN SUBCOMMAND: {subcommand}")
