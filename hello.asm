BITS 64
segment .text

global _start

_start:
  mov rax, 0x2000001
  mov rdi, 69
  syscall 


