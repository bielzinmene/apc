#include <stdio.h>
#include <string.h>

void imprimir_info(const char* mensagem) {
    printf("A mensagem e: %s\n", mensagem);
    printf("Seu tamanho e: %zu\n", strlen(mensagem));
    
}

int main() {
    const char* erro_msg = "Acesso Negado";
    
    imprimir_info(erro_msg);
    
    return 0;
}
