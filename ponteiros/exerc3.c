#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char nome[50];
    float totalCompras;
} Cliente;

// Ordena alfabeticamente usando strcmp (dica do slide 25)
void ordenarPorNome(Cliente *v, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (strcmp(v[j].nome, v[j + 1].nome) > 0) {
                Cliente aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
        }
    }
}

// Ordena por maior valor gasto
void ordenarPorTotalCompras(Cliente *v, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (v[j].totalCompras < v[j + 1].totalCompras) {
                Cliente aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
        }
    }
}

// Busca Binária por Nome (Exige que o vetor esteja ordenado por nome)
int buscaBinariaPorNome(Cliente *v, int n, char *nomeBusca) {
    int inicio = 0, fim = n - 1;
    while (inicio <= fim) {
        int meio = (inicio + fim) / 2;
        int res = strcmp(nomeBusca, v[meio].nome);

        if (res == 0) return meio; // Encontrou
        if (res < 0) fim = meio - 1;
        else inicio = meio + 1;
    }
    return -1; // Não encontrado
}

void imprimirClientes(Cliente *v, int n) {
    printf("\n--- LISTA DE CLIENTES ---\n");
    for (int i = 0; i < n; i++) {
        printf("ID: %d | Nome: %-15s | Total Compras: R$ %.2f\n", 
               v[i].id, v[i].nome, v[i].totalCompras);
    }
}

int main() {
    int n;
    printf("Quantos clientes deseja cadastrar inicialmente? ");
    scanf("%d", &n);

    // Alocação inicial com calloc (slide 10 e 25)
    Cliente *v = calloc(n, sizeof(Cliente));
    if (v == NULL) {
        printf("Erro ao alocar memoria.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("\nCliente %d:\n", i + 1);
        printf("ID: ");
        scanf("%d", &v[i].id);
        printf("Nome: ");
        scanf(" %[^\n]", v[i].nome);
        printf("Total de compras: ");
        scanf("%f", &v[i].totalCompras);
    }

    int opcao;
    do {
        printf("\n=== MENU CLIENTES ===\n");
        printf("1. Ordenar por nome\n");
        printf("2. Ordenar por total de compras\n");
        printf("3. Buscar cliente por nome (Busca Binaria)\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                ordenarPorNome(v, n);
                printf("\nClientes ordenados por NOME:\n");
                imprimirClientes(v, n);
                break;

            case 2:
                ordenarPorTotalCompras(v, n);
                printf("\nClientes ordenados por TOTAL DE COMPRAS:\n");
                imprimirClientes(v, n);
                break;

            case 3: {
                // Garante que o vetor esteja ordenado por nome para a busca funcionar
                ordenarPorNome(v, n);
                
                char busca[50];
                printf("Digite o nome exato para buscar: ");
                scanf(" %[^\n]", busca);

                int idx = buscaBinariaPorNome(v, n, busca);
                if (idx != -1) {
                    printf("\n Cliente encontrado!\n");
                    printf("ID: %d | Nome: %s | Total Compras: R$ %.2f\n", 
                           v[idx].id, v[idx].nome, v[idx].totalCompras);
                } else {
                    printf("\n Cliente nao encontrado.\n");
                }
                break;
            }

            case 0:
                printf("\nEncerrando e liberando memoria...\n");
                break;

            default:
                printf("\nOpcao invalida!\n");
        }
    } while (opcao != 0);

    // Liberação de memória (slides 10 e 11)
    free(v);
    v = NULL;

    return 0;
}
