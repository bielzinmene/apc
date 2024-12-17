#include <stdio.h>

int main(){
    int compet, folhas, quant_folha;
    scanf("%d %d %d", &compet, &folhas, &quant_folha);
    if (compet * quant_folha <= folhas){
        printf("S\n");
    }
    else{
        printf("N\n");
    }
    return 0;
}