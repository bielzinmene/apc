#include <stdio.h>

int main(){

    int n,k, ar[101], cont = 0;
    scanf("%d %d", &n, &k);
    
    for(int i = 0; i < n; i++){
        scanf("%d", &ar[i]);

    }
    // COMPARANDO OS PARES
    for(int i = 0; i < n; i++){
        for(int j = i+1; j <= n-1; j++){  
            if((ar[i] + ar[j]) % k == 0 ){
                cont++;
            }
        }
    }
        printf("%d\n", cont);

    return 0;

}