#include <stdio.h>

int main() {
    char c1, c2, c3;  

    scanf(" %c%c%c", &c1, &c2, &c3);  

    if (c1 == 'X' && c2 == 'O' && c3 == 'X') {
        printf("*\n");  
    }
    else if (c1 == 'X' && c2 == 'X' && c3 == 'O') {
        printf("Alice\n");  
    }
    else if (c1 == 'X' && c2 == 'O' && c3 == 'O') {
        printf("Bob\n");  
    }
    else {
        printf("?\n");
    }

    return 0;
}
