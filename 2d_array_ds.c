#include <stdio.h>

int hourglassSum(int vetor[][6]){
    int highest_hourglass = -9999999;
    int atual_hourglass;


    for(int i = 0; i < 4; i++){

        atual_hourglass = 0;

        for(int j = 0; j < 4; j++){
            atual_hourglass =
            vetor[i][j] + vetor[i][j + 1] + vetor[i][j + 2] +
            vetor[i + 1][j + 1] +
            vetor[i + 2][j] + vetor[i + 2][j + 1] + vetor[i + 2][j + 2]; 
            
            if(atual_hourglass > highest_hourglass){
                highest_hourglass = atual_hourglass;
            }
        }
    }
    return highest_hourglass;

}
int main(){

    int vetor[6][6];

    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++){
            scanf("%d", &vetor[i][j]);
        }
    }
    printf("%d\n", hourglassSum(vetor));

    return 0;
}