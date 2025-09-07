#include <stdio.h>

//n = 10 m = 3
int birthday(int n,int valores_choc[], int d, int m){
    int cont = 0;
    for(int i = 0; i <= n-m; i++){
        int soma = 0;
        for(int j = 0; j < m; j++){
            soma += valores_choc[i+j];
        }
        if(soma == d){
            cont++;
        }
    }
    return cont;
}
    


int main(){
    int n, valores_choc[101], d,m;

    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &valores_choc[i]);
    }
    scanf("%d %d", &d, &m);

    printf("%d\n", birthday(n,valores_choc, d, m));


    return 0;
}