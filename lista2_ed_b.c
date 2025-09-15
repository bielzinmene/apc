#include <stdio.h>

int divisibleSumPairs(int n, int *ar, int k){
    int cont = 0;
    for(int i = 0; i < n; i++){
            for(int j = i+1; j <= n-1; j++){  
                if((*(ar+i) + *(ar+j)) % k == 0 ){
                    cont++;
                }
            }
        }
    return cont;
}

int main(){

    int n,k, ar[101];
    scanf("%d %d", &n, &k);
    
    for(int i = 0; i < n; i++){
        scanf("%d", &ar[i]);

    }
    
    printf("%d\n", divisibleSumPairs(n,ar,k));

    return 0;

}