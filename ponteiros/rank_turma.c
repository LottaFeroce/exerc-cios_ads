#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int matricula;
    char nome[50];
    float nota;
} Aluno;

// Bubble Sort adaptado para ordem decrescente de nota (slide 19)
void ordenarPorNota(Aluno *v, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (v[j].nota < v[j + 1].nota) { // < ordena da maior para a menor
                Aluno aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
        }
    }
}

int main() {
    int cap = 2, n = 0; // Começa com capacidade 2
    Aluno *v = malloc(cap * sizeof(Aluno));
    if (v == NULL) {
        printf("Erro ao alocar memoria.\n");
        return 1;
    }

    Aluno a;
    while (1) {
        printf("\nMatricula (0 para sair): ");
        scanf("%d", &a.matricula);
        if (a.matricula == 0) break; // Encerra ao digitar 0

        printf("Nome: ");
        scanf(" %[^\n]", a.nome); // Lê a string com espaços
        printf("Nota: ");
        scanf("%f", &a.nota);

        // Bloco de crescimento dinamico (slides 16 e 17)
        if (n == cap) {
            int novaCap = cap * 2;
            Aluno *tmp = realloc(v, novaCap * sizeof(Aluno));
            if (tmp == NULL) {
                printf("Sem memoria!\n");
                free(v);
                return 1;
            }
            v = tmp;
            cap = novaCap;
            printf(">> Realloc executado! Nova capacidade: %d <<\n", cap);
        }

        v[n] = a;
        n++;
    }

    if (n == 0) {
        printf("Nenhum aluno cadastrado.\n");
        free(v);
        return 0;
    }

    // Ordenação e cálculo da média
    ordenarPorNota(v, n);

    float soma = 0;
    printf("\n=== RANKING DA TURMA ===\n");
    for (int i = 0; i < n; i++) {
        printf("%dº lugar: %s | Matricula: %d | Nota: %.2f\n", 
               i + 1, v[i].nome, v[i].matricula, v[i].nota);
        soma += v[i].nota;
    }

    printf("\nMedia geral da turma: %.2f\n", soma / n);

    // Liberação de memória (slides 10 e 11)
    free(v);
    v = NULL;

    return 0;
}