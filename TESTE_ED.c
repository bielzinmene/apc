#include <stdio.h>
#include <string.h>

// Esta função PROMETE que não vai alterar a string 'mensagem'.
// Isso fica claro para quem usa a função.
void imprimir_info(const char* mensagem) {
    printf("A mensagem e: %s\n", mensagem);
    printf("Seu tamanho e: %zu\n", strlen(mensagem));
    
    // A linha abaixo causaria um ERRO DE COMPILAÇÃO, o que é bom!
    // mensagem[0] = 'a'; 
}

int main() {
    // 'erro_msg' aponta para uma string literal, que é constante.
    const char* erro_msg = "Acesso Negado";
    
    imprimir_info(erro_msg);
    
    return 0;
}