#include <stdio.h>

const char* angryprofessor(int n, int k, int a[]){
    int cont = 0;
    for(int i = 0; i < n; i++){
        if(a[i] <= 0){
            cont++;
        }
    }
    if(cont < k){
        return "YES";
    }
    else{
        return "NO";
    }
}

int main(){
    int t,n,k,a[1001];

    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%d %d", &n, &k);
        for(int casos = 0; casos < n; casos++){
            scanf("%d", &a[casos]);
        }
        printf("%s\n", angryprofessor(n, k,a));
    }

    return 0;
}