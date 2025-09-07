#include <stdio.h>

int main(){

int tempo, h, m, s, r1, r2, r3;

    scanf("%d", &tempo);
    h = tempo / 3600;
    r1 = tempo % 3600;
    m = r1 / 60;
    r2 = r1 % 60;
    s = r2;
    printf("%d:%d:%d\n", h, m, s);

    return 0;
}