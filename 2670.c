#include <stdio.h>

int main(){

    int andar1, andar2, andar3;
    int resp;
    scanf("%d %d %d", &andar1, &andar2, &andar3);

    resp = (andar1 * 2) + (andar3) * 2;
    printf("%d\n", resp);
    
    return 0;
}