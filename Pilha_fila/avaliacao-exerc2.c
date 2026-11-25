
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int numero;
    char cliente[50];
    char item[50];
} Pedido;

typedef struct {
    Pedido *dados;
    int inicio;
    int n;
    int cap;
} FilaPed;

int criarFila(FilaPed *f, int cap) {
    f->dados = malloc((size_t)cap * sizeof(Pedido));
    if (f->dados == NULL) {
        return 0;
    }
    f->inicio = 0;
    f->n = 0;
    f->cap = cap;
    return 1;
}
int enfileirar(FilaPed *f, Pedido p) {
    if (f->n == f->cap) {
        return 0;
    }
    int idx = (f->inicio + f->n) % f->cap;
    f->dados[idx] = p;
    f->n++;
    return 1;
}
int desenfileirar(FilaPed *f, Pedido *removido) {
    if (f->n == 0) {
        return 0;
    }
    *removido = f->dados[f->inicio];
    f->inicio = (f->inicio + 1) % f->cap;
    f->n--;
    return 1;
}
void mostrarFila(const FilaPed *f) {
    if (f->n == 0) {
        printf("\nFila vazia, cadê a grana?\n");
        return;
    }
    printf("\nPedidos esfriando\n");
    for (int i = 0; i < f->n; i++) {
        int idx = (f->inicio + i) % f->cap;

        printf("#%d Cliente: %s Item: %s\n",
               f->dados[idx].numero,
               f->dados[idx].cliente,
               f->dados[idx].item);
    }
}
void destruirPedidos(FilaPed *f) {
    free(f->dados);
    f->dados = NULL;
    f->inicio = 0;
    f->n = 0;
    f->cap = 0;
}
int main() {
    FilaPed fila;
    int cap = 5;
    int proximoNumero = 1;
    int opcao;
    if (!criarFila(&fila, cap)) {
        printf("Erro ao alocar memoria para a fila.\n");
        return 1;
    }
    do {
        printf("\n Lanção do senac\n");
        printf("1 Novo pedido\n");
        printf("2 Entregar o proximo pedido\n");
        printf("3 Mostrar pedidos em espera\n");
        printf("0 Sair\n");
        printf("Escolha: ");
        if (scanf("%d", &opcao) != 1) {
            printf("Entrada invalida.\n");
            break;
        }
        if (opcao == 1) {
            if (fila.n == fila.cap) {
                printf("\nBalcão lotado, sem mais pedidos.\n");
            } else {
                Pedido novo;
                novo.numero = proximoNumero;
                printf("Nome do cliente: ");
                scanf(" %49[^\n]", novo.cliente);
                printf("Item pedido: ");
                scanf(" %49[^\n]", novo.item);
                if (enfileirar(&fila, novo)) {
                    printf("\nPedido #%d cadastrado\n",
                           novo.numero);
                    proximoNumero++;
                }
            }
        } else if (opcao == 2) {
            Pedido atendido;
            if (desenfileirar(&fila, &atendido)) {
                printf("\nPedido entregue... din din$$$\n");
                printf("Numero: #%d\n", atendido.numero);
                printf("Cliente: %s\n", atendido.cliente);
                printf("Item: %s\n", atendido.item);
            } else {
                printf("\nProcura-se clientela.\n");
            }
        } else if (opcao == 3) {
            mostrarFila(&fila);
        } else if (opcao == 0) {
            printf("\nEncerrando o sistema\n");
            destruirPedidos(&fila);
            printf("Memoria liberada\n");
        } else {
            printf("\nOpção invalida.\n");
        }
    } while (opcao != 0);
    destruirPedidos(&fila);
    return 0;
}
