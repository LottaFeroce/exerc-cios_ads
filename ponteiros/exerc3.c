#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char nome[50];
    float total_compras;
} Cliente;

void ordenar_por_nome(Cliente *vetor, int n) {
    for (int indice = 0; indice < n - 1; indice++) {
        for (int indice_interno = 0; indice_interno < n - 1 - indice; indice_interno++) {
            if (strcmp(vetor[indice_interno].nome, vetor[indice_interno + 1].nome) > 0) {
                Cliente auxiliar = vetor[indice_interno];
                vetor[indice_interno] = vetor[indice_interno + 1];
                v[indice_interno + 1] = auxiliar;
            }
        }
    }
}
void ordenar_por_total_compras(Cliente *vetor, int n) {
    for (int indice = 0; indice < n - 1; indice++) {
        for (int indice_interno = 0; indice_interno < n - 1 - indice; indice_interno++) {
            if (vetor[indice_interno].total_compras < vetor[indice_interno + 1].total_compras) {
                Cliente auxiliar = vetor[indice_interno];
                vetor[indice_interno] = vetor[indice_interno + 1];
                v[indice_interno + 1] = auxiliar;
            }
        }
    }
}
int busca_binaria_por_nome(Cliente *vetor, int n, char *nomeBusca) {
    int inicio = 0, fim = n - 1;
    while (inicio <= fim) {
        int meio = (inicio + fim) / 2;
        int res = strcmp(nomeBusca, vetor[meio].nome);
        if (res == 0) return meio; 
        if (res < 0) fim = meio - 1;
        else inicio = meio + 1;
    }
    return -1; 
}
void imprimir_clientes(Cliente *vetor, int n) {
    printf("\nLista de Clientes: \n");
    for (int indice = 0; indice < n; indice++) {
        printf("ID: %d | Nome: %-15s | Total Compras: R$ %.2f\n", 
               vetor[indice].id, vetor[indice].nome, vetor[indice].total_compras);
    }
}
int main() {
    int n;
    printf("Quantos clientes deseja cadastrar inicialmente? ");
    scanf("%d", &n);

    Cliente *vetor = calloc(n, sizeof(Cliente));
    if (vetor == NULL) {
        printf("Erro ao alocar memoria.\n");
        return 1;
    }
    for (int indice = 0; indice < n; indice++) {
        printf("\nCliente %d:\n", indice + 1);
        printf("ID: ");
        scanf("%d", &vetor[indice].id);
        printf("Nome: ");
        scanf(" %[^\n]", vetor[indice].nome);
        printf("Total de compras: ");
        scanf("%f", &vetor[indice].total_compras);
    }
    int opcao;
    do {
        printf("\nMenu Clientes: \n");
        printf("1. Ordenar por nome\n");
        printf("2. Ordenar por total de compras\n");
        printf("3. Buscar cliente por nome (Busca Binaria)\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                ordenar_por_nome(vetor, n);
                printf("\nClientes ordenados por NOME:\n");
                imprimir_clientes(vetor, n);
                break;
            case 2:
                ordenar_por_total_compras(vetor, n);
                printf("\nClientes ordenados por TOTAL DE COMPRAS:\n");
                imprimir_clientes(vetor, n);
                break;
            case 3: {
                ordenar_por_nome(vetor, n);          
                char busca[50];
                printf("Digite o nome exato para buscar: ");
                scanf(" %[^\n]", busca);
                int idx = busca_binaria_por_nome(vetor, n, busca);
                if (idx != -1) {
                    printf("\n Cliente encontrado!\n");
                    printf("ID: %d | Nome: %s | Total Compras: R$ %.2f\n", 
                           vetor[idx].id, vetor[idx].nome, vetor[idx].total_compras);
                } else {
                    printf("\n Cliente nao encontrado.\n");
                }
                break;
            }
            case 0:
                printf("\nEncerrando e liberando memoria\n");
                break;
            default:
                printf("\nOpcao invalida\n");
        }
    } while (opcao != 0);
    free(vetor);
    vetor = NULL;
    return 0;
}
