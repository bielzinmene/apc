#include <stdio.h>

int main(){

    int matriz[12][12];
    int l;
    double soma;
    char op;

    scanf("%d", &l);
    getchar();
    scanf("%c", &op);

    for(int i = 0; i < 12; i++){
        for(int j = 0; j < 12; i++){
            scanf("%d", &matriz[i][j]);
        }
    }

    for(int i = 0; i < 12; i++){
        for(int j = 0; j < 12; i++){
        soma += matriz[i][j];
        }
    }

    if(op == 'S'){
        printf("%.1lf", soma);
    }
    else{
        printf("%.1lf", soma/144);
    }


    return 0;
}