#include <stdio.h>
int somaVetor(int *vetor, int n){
    int soma = 0;
    for(int i = 0; i < n; i++){
        
        soma += *(vetor+i);

    }
    return soma;
}

int main(){

    int n, vetor[101];
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        scanf("%d", &vetor[i]);

    }
    printf("%d\n", somaVetor(vetor, n));

    return 0;
}