#!/usr/bin/env python3

import sys
import subprocess

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


def compile(program, file):
    with open(file, "w") as file:
        file.write("BITS 64\n")
        file.write("segment .text\n")
        file.write("dump:\n")
        file.write("\t mov  r8, -3689348814741910323\n")
        file.write("\t sub     rsp, 40\n")
        file.write("\t mov     BYTE [rsp+31], 10\n")
        file.write("\t lea     rcx, [rsp+30]\n")
        file.write(".L2:\n")
        file.write("\t mov rax, rdi\n")
        file.write("\t mul r8\n")
        file.write("\t mov rax, rdi\n")
        file.write("\t shr rdx, 3\n")
        file.write("\t lea rsi, [rdx+rdx*4]\n")
        file.write("\t add rsi, rsi\n")
        file.write("\t sub rax, rsi\n")
        file.write("\t mov rsi, rcx\n")
        file.write("\t sub     rcx, 1\n")
        file.write("\t add     eax, 48\n")
        file.write("\t mov     BYTE [rcx+1], al\n")
        file.write("\t mov     rax, rdi\n")
        file.write("\t mov     rdi, rdx\n")
        file.write("\t cmp     rax, 9\n\n")
        file.write("\t ja      .L2\n")
        file.write("\t lea     rdx, [rsp+32]\n")
        file.write("\t mov     edi, 1\n")
        file.write("\t xor     eax, eax\n")
        file.write("\t sub     rdx, rsi\n")
        file.write("\t mov     rax, 1\n")
        file.write("\t syscall\n")
        file.write("\t add     rsp, 40\n")
        file.write("\t ret\n")
        file.write("global _start\n")
        file.write("_start:\n")
        for op in program:
            assert COUNT_OPS == 4, "Exhaustive use of ops in compilation"
            if op[0] == OP_PUSH:
                file.write(";; -- push ---\n")
                file.write("\t push %d\n" % op[1])
            elif op[0] == OP_PLUS:
                file.write(";; -- plus ---\n")
                file.write("\t pop rbx\n")
                file.write("\t pop rcx\n")
                file.write("\t add rbx, rcx\n")
                file.write("\t push rbx\n")
            elif op[0] == OP_MINUS:
                file.write(";; -- minus ---\n")
                file.write("\t pop rbx\n")
                file.write("\t pop rcx\n")
                file.write("\t sub rcx, rbx\n")
                file.write("\t push rcx\n")
            elif op[0] == OP_DUMP:
                file.write(";; -- dump ---\n")
                file.write("\t pop rdi\n")
                file.write("\t call dump\n")

            else:
                assert "unreachable"
        file.write(";; -- exit syscall ---\n")
        file.write("\t mov rax, 60\n")
        file.write("\t mov rdi, 69\n")
        file.write("\t syscall\n")


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


def call_command(command):
    print(command)
    subprocess.call(command)


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
        compile(program=program, file="output.asm")
        call_command(["nasm", "-felf64", "output.asm", "-o", "output.o"])
        call_command(["ld", "-o", "output", "output.o"])
    else:
        print(f"UNKNOWN SUBCOMMAND: {subcommand}")
