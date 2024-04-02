#makefile for linux

main:main.o
	ld -o $@ $^

main.o:main.asm
	nasm -felf64 $^ -o $@


clean:
	rm main && rm main.o
