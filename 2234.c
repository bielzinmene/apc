#include <stdio.h>

    int main(){

    int cac, part;
    double tempo;

    scanf("%d %d", &cac, &part);
    tempo = cac / (double)part;
    printf("%.2lf\n", tempo);


    return 0;

}