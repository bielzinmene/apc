#include <stdio.h>

    int main(){
    
    int a, b, c;
    double result;
    scanf("%d %d %d", &a, &b, &c);
    result = (double)a / b;
    printf("%.2lf\n", result / c);

    return 0;



    }