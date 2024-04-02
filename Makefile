main: main.o
	ld -arch x86_64 -e _start -static $^ -o $@

main.o: hello.asm
	nasm -f macho64 $^ -o $@

clean:
	rm main.o && rm main
