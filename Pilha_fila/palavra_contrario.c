#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *dados;
    int topo;
    int cap;
} PilhaChar;

int criarPilha(PilhaChar *p, int cap) {
    p->dados = malloc(cap * sizeof(char));
    if (p->dados == NULL) return 0;
    p->topo = 0;
    p->cap = cap;
    return 1;
}

int empilhar(PilhaChar *p, char c) {
    if (p->topo == p->cap) {
        int nova = 2 * p->cap;
        char *tmp = realloc(p->dados, nova * sizeof(char));
        if (tmp == NULL) return 0;
        p->dados = tmp;
        p->cap = nova;
    }
    p->dados[p->topo] = c;
    p->topo++;
    return 1;
}

int desempilhar(PilhaChar *p, char *c) {
    if (p->topo == 0) return 0;
    p->topo--;
    *c = p->dados[p->topo];
    return 1;
}

void destruirPilha(PilhaChar *p) {
    free(p->dados);
    p->dados = NULL;
    p->topo = 0;
    p->cap = 0;
}

int main(void) {
    char palavra[101];
    printf("Digite uma palavra (ate 100 letras): ");
    if (scanf("%100s", palavra) != 1) return 1;

    PilhaChar p;
    if (!criarPilha(&p, 4)) return 1;

    size_t tam = strlen(palavra);
    for (size_t i = 0; i < tam; i++) {
        empilhar(&p, palavra[i]);
    }

    char invertida[101];
    char c;
    int idx = 0;

    printf("Saida: ");
    while (desempilhar(&p, &c)) {
        putchar(c);
        invertida[idx++] = c;
    }
    invertida[idx] = '\0';
    printf("\n");

    // Extra: Que loucura é essa Caleb??
    if (strcmp(palavra, invertida) == 0) {
        printf("E-> palindromo\n");
    } else {
        printf("Nao <-e palindromo.\n");
    }

    destruirPilha(&p);
    return 0;
}