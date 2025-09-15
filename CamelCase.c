#include <stdio.h>
#include <string.h>

int camelcase(char *string){
    int cont = 0;
    int tamanho_string = strlen(string);
    for(int i = 0; i < tamanho_string; i++){
        if(*(string+i) <= 90 && *(string+i) >=65){
            cont++;
        } 
    }
    return cont + 1;
}

int main(){

    char string[1000001];
    scanf("%s", string);
    printf("%d\n", camelcase(string));

    return 0;
}