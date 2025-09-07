void plusMinus(int tam){
    int array[101];
    int quant_pos = 0, quant_neg = 0, quant_zero = 0;


    for(int i = 0; i < tam; i++){
        scanf("%d", &array[i]);
    }

    for(int i = 0; i < tam; i++){
        if(array[i] > 0){
            quant_pos++;
        }
        else if(array[i] < 0){
            quant_neg++;
        }
        else{
            quant_zero++;
        }
    }
    printf("%.5lf\n%.5lf\n%.5lf\n", 
        (double)quant_pos/tam, 
        (double)quant_neg/tam, 
        (double)quant_zero/tam);
}





int main(){
    int n;
    scanf("%d", &n);
    plusMinus(n);

    return 0;
}