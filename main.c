#include<stdlib.h>
#include <stdint.h>
#include<unistd.h>

#define BUF_CAP 32

void dump(uint64_t x){

    char buf[32];
    size_t buf_size = 1;

    buf[sizeof(buf) - buf_size] = '\n';

    do{
        buf[(sizeof(buf) - buf_size) - 1]= x % 10 + '0';
        buf_size ++;
        x /=10;
    }while(x);

    write(1, &buf[sizeof(buf) - buf_size], buf_size);
}


int main()
{
    dump(69420);
    dump(1);

}
