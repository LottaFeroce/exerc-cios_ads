#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    char *dados;
    int topo;
    int capacidade;
} PilhaString;
int criarPilha(PilhaString *p, int capacidade) {
    p->dados = malloc(capacidade * sizeof(char));
    if (p->dados == NULL) return 0;
    p->topo = 0;
    p->capacidade = capacidade;
    return 1;}
int colocanaPilha(PilhaString *p, char c) {
    if (p->topo == p->capacidade) {
        int nova_capacidade = 2 * p->capacidade;
        char *Temporario = realloc(p->dados, nova_capacidade * sizeof(char));
        if (Temporario == NULL) return 0;
        p->dados = Temporario;
        p->capacidade = nova_capacidade;
    }    p->dados[p->topo] = c;
    p->topo++;
    return 1;
}
int tiradaPilha(PilhaString *p, char *c) {
    if (p->topo == 0) return 0;
    p->topo--;
    *c = p->dados[p->topo];
    return 1;
}
void rePilha(PilhaString *p) {
    free(p->dados);
    p->dados = NULL;
    p->topo = 0;
    p->capacidade = 0;
}
int main(void) {
    char senha[101];
    printf("Digite uma senha com no maxímo 100 letras:-> ");
    if (scanf("%100s", senha) != 1) return 1;
    PilhaString p;
    if (!criarPilha(&p, 4)) return 1;
    size_t tam = strlen(senha);
    for (size_t i = 0; i < tam; i++) {
        colocanaPilha(&p, senha[i]);
    }
    char invertida[101];
    char c;
    int idx = 0;
    printf("Saida: ");
    while (tiradaPilha(&p, &c)) {
        putchar(c);
        invertida[idx++] = c;
    }
    invertida[idx] = '\0';
    printf("\n");
    // Agente secreto perguntando sobre Palindröpos???
    if (strcmp(senha, invertida) == 0) {
        printf("É-> palindromo\n");
    } else {
        printf("Não <-é palindromo.\n");
    }
    rePilha(&p);
    return 0;
}