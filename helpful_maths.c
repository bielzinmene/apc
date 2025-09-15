#include <stdio.h>
#include <string.h>

int main(){
    char string[101];
    char string_alterada[101];
    int cont_1 = 0, cont_2 = 0, cont_3 = 0;


    scanf("%s", string);

    for(int i = 0; string[i] != '\0'; i++){
        
        if(string[i] == '1'){
            cont_1++;
        }
        else if(string[i] == '2'){
            cont_2++;
        }
        else if(string[i] == '3'){
            cont_3++;
        }

    }
    int k = 0; 

    while (cont_1 > 0) {
        string_alterada[k++] = '1';
        string_alterada[k++] = '+';
        cont_1--;
    }

    while (cont_2 > 0) {
        string_alterada[k++] = '2';
        string_alterada[k++] = '+';
        cont_2--;
    }

    while (cont_3 > 0) {
        string_alterada[k++] = '3';
        string_alterada[k++] = '+';
        cont_3--;
    }

    if (k > 0) {
        string_alterada[k - 1] = '\0'; 
    }
    printf("%s\n", string_alterada);

    return 0;
}