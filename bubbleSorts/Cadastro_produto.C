#include <stdio.h>
#<include <string.h>

#define MAX_PRODUTOS 100

//Essa é a função que define a estrutura do produto
typedef struct {
    int codigo;
    char nome[50];
    float preco;
    int quantidade;
} Produto;

//função para imprimir os produtos cadastrados
void imprimir_produtos(Produto produtos[], int quant){
    if(quant == 0) {
        printf("Nenhum produto cadastrado.\n");
        return;
    }
    printf("\n <-- Lista de Produtos Cadastrados -->\n");
    for(int i = 0; i < quant; i++){
        printf("Codigo: %d | Nome: %s | Preco: %.2f | Quantidade: %d\n", produtos[i].codigo, produtos[i].nome, produtos[i].preco, produtos[i].quantidade);
    }
}

//Função para ordenar os produtos por preço usando o algoritmo bubble sort
void ordernar_preco(Produto produtos[], int quant){
    produto temp;
    for(int i = 0; i < quant - 1; i++){
        for(int j = 0; j < quant - i - 1; j++){
            if(produtos[j].preco > produtos[j + 1].preco){
                temp = produtos[j];
                produtos[j] = produtos[j + 1];
                produtos[j + 1] = temp;
            }
        }
    }
    printf("\nProdutos ordenados por preco com sucesso\n");
}

//Função para ordenar os produtos por código utilizando busca binária
void ordenar_codigo(Produto produtos[], int quant){
    produto temp;
    for(int i = 0; i < quant - 1; i++){
        for(int j = 0; j < quant - i - 1; j++){
            if(produtos[j].codigo > produtos[j + 1].codigo){
                temp = produtos[j];
                produtos[j] = produtos[j + 1];
                produtos[j + 1] = temp;
            }
        }
    }
    printf("\nProdutos ordenados por codigo com sucesso\n");
}


//Função de busca binária para encontrar um produto pelo código
int busca_binaria(Produto produtos[], int quant, int codigo){
    int inicio = 0;
    int fim = quant - 1;
    while(inicio <= fim){
        int meio = (inicio + fim) / 2;
        if(produtos[meio].codigo == codigo){
            return meio; // Produto encontrado
        } else if(produtos[meio].codigo < codigo){
            inicio = meio + 1; // Procurar na metade direita
        } else {
            fim = meio - 1; // Procurar na metade esquerda
        }
    }
    return -1; // Produto não encontrado
}

//Função para calcular e exibir o valor total do estoque
void calcular_valor_estoque(Produto produtos[], int quant){
    float valor_total = 0;
    for(int i = 0; i < quant; i++){
        valor_total += produtos[i].preco * produtos[i].quantidade;
    }
    printf("\nValor total do estoque: %.2f\n", valor_total);
}

int main(){
    Produto estoque[MAX_PRODUTOS];
    int quant_produtos = 0;
    int opcao, codigo_busca, posicao;

    do{
        printf("\n--- Menu em relação aos Produtos ---\n");
        printf("1. Cadastrar Produto\n");
        printf("2. Listar Produtos\n");
        printf("3. Ordenar Produtos por Preco\n");
        printf("4. Ordenar Produtos por Codigo\n");
        printf("5. exibir Valor Total do Estoque\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao){
            case 1:
            printf("\nQuantos produtos deseja cadastrar? ");
            int quantidade;
            scanf("%d", &quantidade);
            for(int item = 0; item < quantidade; item++){
                if(quant_produtos >= MAX_PRODUTOS){
                    printf("Limite de produtos atingido.\n");
                    break;
                }
                printf("\nCadastro do Produto %d:\n", quant_produtos + 1);
                printf("Codigo: ");
                scanf("%d", &estoque[quant_produtos].codigo);
                printf("Nome: ");
                scanf(" %[^\n]s", estoque[quant_produtos].nome); // Lê até a nova linha
                printf("Preco: ");
                scanf("%f", &estoque[quant_produtos].preco);
                printf("Quantidade: ");
                scanf("%d", &estoque[quant_produtos].quantidade);
                quant_produtos++;
            }
            break;
        case 2:
            imprimir_produtos(estoque, quant_produtos);
            break; 

        case 3:
            ordernar_preco(estoque, quant_produtos);
            imprimir_produtos(estoque, quant_produtos);
            break;

        case 4:
            if (quant_produtos == 0) {
                printf("\nNenhum produto cadastrado para busca.\n");
                break;
            }
            //para executar a busca binária, o vetor precisa estar ordenado por código
            ordenar_codigo(estoque, quant_produtos);

            printf("\nDigite o codigo do produto que deseja buscar: ");
            scanf("%d", &codigo_busca);

            posicao = busca_binaria(estoque, quant_produtos, codigo_busca);
            if(posicao != -1){
                printf("\nProduto encontrado:\n");
                printf("Codigo: %d | Nome: %s | Preco: %.2f | Quantidade: %d\n", estoque[posicao].codigo, estoque[posicao].nome, estoque[posicao].preco, estoque[posicao].quantidade);
            } else {
                printf("\nProduto nao encontrado.\n");
            }
            break;

        case 5:
            calcular_valor_estoque(estoque, quant_produtos);
            break;
        case 0:
            printf("Saindo do programa\n");
            break;
        default:
            printf("Opcao invalida. Tente novamente.\n");

        }
    }while(opcao != 0);
    return 0;
}