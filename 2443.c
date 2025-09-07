#include <stdio.h>

int main(){

    int a,b,c,d, ans;

    scanf("%d %d %d %d", &a,&b,&c,&d);

    if(b == d){
        ans = (a*c)/(b);
    }
    else{
        ans = (a*d)+(b*c)/(b*d);
    }

    printf("%d\n", ans);




    return 0;
}