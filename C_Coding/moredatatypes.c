#include<stdio.h>
#include<stdbool.h>

int main(int argc, char const *argv[])
{
    char a = "C"; // single characters %c
    char b[] = "Gab"; // array of characters %s

    float c = 3.1453; // 4 bytes (32 bits precision) 6-7 digits %f
    double d = 3.145323423423235; // 8 bytes (64 bits precision) 15-16 digits %lf

    bool e = true; // 1 byte (true or false) %d

    char f = 120; // 1 byte (-128 to 127) %d for int and %c for this number as char
    unsigned char g = 255; // 1 byte (0 to 255) %d or %c

    short int h  = 32767; // 2 bytes (-32,768 to 32,767) %d
    unsigned short int i = 65000; // 2 bytes ( 0 to +65,535) %d

    int j = 2147483647; // 4 bytes (-2147483648 to 2147483647) %d
    unsigned int k = 4290999999; // 4 byter (0 to 4294967295) %u

 
    return 0;
}