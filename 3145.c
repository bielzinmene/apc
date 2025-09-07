#include <stdio.h>

int main(){
    int n, x;
    double dias;
    scanf("%d %d", &n, &x);
    dias = ((double)n + 2);
    printf("%.2lf", x / dias);
    return 0;

 
}