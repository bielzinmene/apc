#include <stdio.h>
#include <stdlib.h>

int *rotLeft(int n, int d, int *a) {
    int *vetor_rotacionado = malloc(n * sizeof(int));
    
    if (vetor_rotacionado == NULL) {
        return NULL;
    }

    for (int i = 0; i < n - d; i++) {
        vetor_rotacionado[i] = a[d + i];
    }

    for (int i = 0; i < d; i++) {
        vetor_rotacionado[n - d + i] = a[i];
    }

    return vetor_rotacionado;
}

int main(){

    int n, d;

    scanf("%d %d", &n, &d);
    
    int a[n];

    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    
    int *resultado = rotLeft(n, d, a);

    if (resultado != NULL) {
        for (int i = 0; i < n; i++) {
            printf("%d ", resultado[i]);
        }
        printf("\n");

        free(resultado);
    }

    return 0;
}