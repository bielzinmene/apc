#include <stdio.h>

int main(){
    int n,r, retornaram;

    while(scanf("%d %d", &n,&r) != -1){

        int vivos[10002];

        for(int i=1; i <= n; i++){
            vivos[i] = 0;
        }

        for(int i=1; i<=r; i++){
            scanf("%d", &retornaram);

            vivos[retornaram]=1;

        }
        if(n == r){
            printf("*");
        }
        else{

            for(int i=1; i<n+1; i++){
                if(vivos[i] != 1){
                    printf("%d ", i);
                }
            }
        }

        printf("\n");
        
    }

    return 0;
}
