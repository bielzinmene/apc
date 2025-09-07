#include <stdio.h>

int main(){
    int peca, num_pec, peca2, num_pec2;
    double valor_pe, valor_pe2, total;

    scanf("%d %d %lf %d %d %lf", &peca, &num_pec, &valor_pe, &peca2, &num_pec2, &valor_pe2);
    total = (num_pec * valor_pe) + (num_pec2 * valor_pe2);
    printf("VALOR A PAGAR: R$ %.2lf\n", total);

    return 0;
}