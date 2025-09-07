void catAndMouse(int cat1, int cat2, int mouse){
    int dist_cat1, dist_cat2;
    dist_cat1 = abs(cat1 - mouse);
    dist_cat2 = abs(cat2 - mouse);
    if(dist_cat1 < dist_cat2){
        printf("Cat A\n");
    }
    else if(dist_cat1 == dist_cat2){
        printf("Mouse C\n");
    }
    else{
        printf("Cat B\n");
    }
}




#include <stdio.h>
#include <stdlib.h>

int main(){
    int testes;
    scanf("%d", &testes);
    for(int i = 0; i < testes; i++){
        int x,y,z;
        scanf("%d %d %d", &x,&y,&z);
        catAndMouse(x,y,z);
    }

    return 0;
}