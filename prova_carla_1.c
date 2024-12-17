#include <stdio.h>

int main(){

    int bandejas, latas, copos;
    scanf("%d", &bandejas);

    int count = 0;

    for(int i = 0; i < bandejas; i++){
        scanf("%d %d", &latas, &copos);
        if (latas > copos){
            count += copos;

        }

    }
    printf("%d", count);

    return 0;

}