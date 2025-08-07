#include <stdio.h>

int main() {
    unsigned char A = 0x55; // 0101 0101
    unsigned char B = 0xF0; // 1111 0000
    unsigned char X;

    // a) A & B
    X = A & B;
    printf("a) X = A & B  -> 0x%02X\n", X);

    // b) A | B
    X = A | B;
    printf("b) X = A | B  -> 0x%02X\n", X);

    // c) A && B (lógico)
    X = A && B;
    printf("c) X = A && B -> %d\n", X);

    // d) A || B (lógico)
    X = A || B;
    printf("d) X = A || B -> %d\n", X);

    // e) B >> 4
    X = B >> 4;
    printf("e) X = B >> 4 -> 0x%02X\n", X);

    // f) A << 1
    X = A << 1;
    printf("f) X = A << 1 -> 0x%02X\n", X);

    return 0;
}
