#include <stdio.h>

void trocaValores(int *a, int *b){
    int aux;
    aux = *b;
    *b = *a;
    *a = aux;
    printf("%d %d", *a,*b);


}
int main(){
    int a,b;
    scanf("%d %d", &a, &b);

    printf("Valor de a -> %d e b -> %d antes da função\n", a,b);

    trocaValores(&a,&b);



    return 0;
}