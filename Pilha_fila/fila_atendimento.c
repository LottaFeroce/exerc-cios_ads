#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int senha;
    char nome[50];
} Paciente;

typedef struct {
    Paciente *dados;
    int inicio, n, cap;
} FilaPac;

int criarFila(FilaPac *f, int cap) {
    f->dados = malloc(cap * sizeof(Paciente));
    if (f->dados == NULL) return 0;
    f->inicio = 0;
    f->n = 0;
    f->cap = cap;
    return 1;
}

int enfileirar(FilaPac *f, Paciente pac) {
    if (f->n == f->cap) return 0; // fila cheia
    int fim = (f->inicio + f->n) % f->cap;
    f->dados[fim] = pac;
    f->n++;
    return 1;
}

int desenfileirar(FilaPac *f, Paciente *pac) {
    if (f->n == 0) return 0; // fila vazia
    *pac = f->dados[f->inicio];
    f->inicio = (f->inicio + 1) % f->cap;
    f->n--;
    return 1;
}

void mostrarFila(const FilaPac *f) {
    if (f->n == 0) {
        printf("Fila vazia.\n");
        return;
    }
    printf("--- Fila atual ---\n");
    for (int i = 0; i < f->n; i++) {
        int pos = (f->inicio + i) % f->cap;
        printf("Senha %d - %s\n", f->dados[pos].senha, f->dados[pos].nome);
    }
}

int main(void) {
    FilaPac fila;
    if (!criarFila(&fila, 5)) return 1;

    int opcao, proximaSenha = 1;

    do {
        printf("\n1. Chegada | 2. Chamar proximo | 3. Mostrar fila | 0. Sair\nEscolha: ");
        if (scanf("%d", &opcao) != 1) break;
        getchar(); // consome '\n' pendente

        if (opcao == 1) {
            if (fila.n == fila.cap) {
                printf("Fila cheia! Nao foi possivel cadastrar.\n");
            } else {
                Paciente novo;
                novo.senha = proximaSenha++;
                printf("Nome do paciente: ");
                fgets(novo.nome, sizeof(novo.nome), stdin);
                novo.nome[strcspn(novo.nome, "\n")] = '\0';

                enfileirar(&fila, novo);
                printf("Cadastrado com senha %d.\n", novo.senha);
            }
        } else if (opcao == 2) {
            Paciente chamado;
            if (!desenfileirar(&fila, &chamado)) {
                printf("Fila vazia! Ninguem para chamar.\n");
            } else {
                printf("Chamando -> Senha %d: %s\n", chamado.senha, chamado.nome);
            }
        } else if (opcao == 3) {
            mostrarFila(&fila);
        }
    } while (opcao != 0);

    free(fila.dados);
    printf("Encerrando e liberando memoria.\n");
    return 0;
}