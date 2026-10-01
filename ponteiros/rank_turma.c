#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int matricula;
    char nome[50];
    float nota;
} Aluno;
void Ordenar_por_nota(Aluno *vetor, int n) {
    for (int indice = 0; indice < n - 1; indice++) {
        for (int indice_interno = 0; indice_interno < n - 1 - indice; indice_interno++) {
            if (vetor[indice_interno].nota < vetor[indice_interno + 1].nota) { 
                Aluno auxiliar = vetor[indice_interno];
                vetor[indice_interno] = vetor[indice_interno + 1];
                v[indice_interno + 1] = auxiliar;
            }
        }
    }
}

int main() {
    int capacidade = 2, n = 0; 
    Aluno *vetor = malloc(capacidade * sizeof(Aluno));
    if (vetor == NULL) {
        printf("Erro ao alocar memoria.\n");
        return 1;
    }
    Aluno aluno1;
    while (1) {
        printf("\nMatricula (0 para sair): ");
        scanf("%d", &aluno1.matricula);
        if (aluno1.matricula == 0) break; 
        printf("Nome: ");
        scanf(" %[^\n]", aluno1.nome); 
        printf("Nota: ");
        scanf("%f", &aluno1.nota);
        if (n == capacidade) {
            int nova_capacidade = capacidade * 2;
            Aluno *temporario = realloc(vetor, nova_capacidade * sizeof(Aluno));
            if (temporario == NULL) {
                printf("Sem memoria!\n");
                free(v);
                return 1;
            }
            vetor = temporario;
            capacidade = nova_capacidade;
            printf(">> Realloc executado! Nova capacidade: %d <<\n", capacidade);
        }
        vetor[n] = aluno1;
        n++;
    }
    if (n == 0) {
        printf("Nenhum aluno cadastrado.\n");
        free(v);
        return 0;
    }
    Ordenar_por_nota(vetor, n);

    float soma = 0;
    printf("\nRanking de turma\n");
    for (int indice = 0; indice < n; indice++) {
        printf("%dº lugar: %s | Matricula: %d | Nota: %.2f\n", 
               indice + 1, vetor[indice].nome, vetor[indice].matricula, vetor[indice].nota);
        soma += vetor[indice].nota;
    }
    printf("\nMedia geral da turma: %.2f\n", soma / n);
    free(vetor);
    vetor = NULL;
    return 0;
}