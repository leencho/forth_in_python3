BITS 64
segment .text

global _start

_start:
  mov rax, 0x2000001 # macos exit syscall
  mov rdi, 69
  syscall 


