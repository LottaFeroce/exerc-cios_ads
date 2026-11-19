#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *dados;
    int topo;
    int cap;
} PilhaInt;

int criarPilha(PilhaInt *p, int cap) {
    p->dados = malloc(cap * sizeof(int));
    if (p->dados == NULL) return 0;
    p->topo = 0;
    p->cap = cap;
    return 1;
}

int empilhar(PilhaInt *p, int x) {
    if (p->topo == p->cap) {
        int nova = 2 * p->cap;
        int *tmp = realloc(p->dados, nova * sizeof(int));
        if (tmp == NULL) return 0;
        p->dados = tmp;
        p->cap = nova;
    }
    p->dados[p->topo++] = x;
    return 1;
}

int desempilhar(PilhaInt *p, int *x) {
    if (p->topo == 0) return 0;
    p->topo--;
    *x = p->dados[p->topo];
    return 1;
}

int calcular(int a, int b, char op, int *ok) {
    *ok = 1;
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) {
                *ok = 0;
                return 0;
            }
            return a / b;
        default:
            *ok = 0;
            return 0;
    }
}

int main(void) {
    char expr[256];
    printf("Digite a expressao pos-fixa: ");
    if (fgets(expr, sizeof(expr), stdin) == NULL) return 1;

    PilhaInt p;
    if (!criarPilha(&p, 16)) return 1;

    int valida = 1;

    for (int i = 0; expr[i] != '\0'; i++) {
        char c = expr[i];
        if (c == ' ' || c == '\n' || c == '\r') continue;

        if (c >= '0' && c <= '9') {
            if (!empilhar(&p, c - '0')) {
                valida = 0;
                break;
            }
        } else {
            int a, b, okCalc;
            if (!desempilhar(&p, &b) || !desempilhar(&p, &a)) {
                valida = 0;
                break;
            }
            int res = calcular(a, b, c, &okCalc);
            if (!okCalc || !empilhar(&p, res)) {
                valida = 0;
                break;
            }
        }
    }

    int resultado;
    if (!valida || p.topo != 1 || !desempilhar(&p, &resultado)) {
        printf("Expressao invalida\n");
    } else {
        printf("%d\n", resultado);
    }

    free(p.dados);
    return 0;
}