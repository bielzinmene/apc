#include <stdio.h>
#include <string.h>

int main(){

    int casos, força;
    char nome[10001];
    
    scanf("%d", &casos);


    for(int i = 0; i < casos; i++){

    scanf("%s %d", nome, &força);
    
        if(strcmp(nome, "Thor") == 0){
            printf("Y\n");
        }
        else{
            printf("N\n");
        }



    }

    return 0;
}