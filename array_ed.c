int simpleArraySum(int espaco){
    int sum = 0, valores;

    for(int i = 0; i < espaco; i++){
        scanf("%d", &valores);
        sum += valores;
    }
    return sum;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", simpleArraySum(n));

    return 0;
}