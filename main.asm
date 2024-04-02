BITS 64

segment .text
global _start
_start:
    mov rax, 60
    mov rdi, 69
    syscall

segment .bss
