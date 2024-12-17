#include <stdio.h>
#include <math.h>

int main(){
    int casos, n, x, y;
    
    // Lê o número de casos de teste
    scanf("%d", &casos);

    for(int i = 0; i < casos; i++){
        // Lê o número de bolas disponíveis (sem contar a branca)
        scanf("%d", &n);

        // Lê a posição da bola branca
        int x_branca, y_branca;
        scanf("%d %d", &x_branca, &y_branca);

        // Inicializa as variáveis para calcular a bola mais próxima
        int menor_distancia = -1;  // A distância mínima inicial é indefinida
        int bola_mais_proxima = -1;

        // Processa as bolas 1 a N
        for(int j = 1; j <= n; j++){
            // Lê a posição da bola j
            scanf("%d %d", &x, &y);

            // Calcula a distância quadrada da bola branca à bola j
            int dist_quadrada = (x - x_branca) * (x - x_branca) + (y - y_branca) * (y - y_branca);

            // Se a distância da bola j for menor que a atual, ou se for igual e a bola for de número menor
            if (menor_distancia == -1 || dist_quadrada < menor_distancia) {
                menor_distancia = dist_quadrada;
                bola_mais_proxima = j;
            }
        }

        // Imprime o número da bola mais próxima
        printf("%d\n", bola_mais_proxima);
    }

    return 0;
}
