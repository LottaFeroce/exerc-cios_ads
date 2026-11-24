Boa tarde! Com base no material da Aula 06 (UC 21), sua avaliação vai focar nos fundamentos, na implementação em C com ponteiros (Pilha *p e Fila *f) e nas regras operacionais de Pilha (LIFO) e Fila Circular (FIFO).
Os pontos que costumam ter maior peso nesse tipo de prova envolvem a convenção de topo (quantidade e próxima posição livre na pilha), o crescimento dinâmico com realloc, o cálculo circular com % cap usando inicio e n na fila, e a atenção a casos de borda como underflow, overflow e passagem por referência.
Abaixo estão 4 exercícios simulados no estilo do que costuma ser cobrado, seguidos das respectivas resoluções em C.
Exercício 1 — Rastreio de Pilha (LIFO) e Verificação de Parênteses
Considere uma pilha inicialmente vazia (topo = 0).
 * Faça o rastreio do estado da pilha (base -> topo) e do valor de topo após as operações:
   empilhar(10), empilhar(20), desempilhar(), empilhar(30), empilhar(40), desempilhar().
 * Aplique a lógica de parênteses/colchetes/chaves balanceados às expressões abaixo e diga qual é válida e qual é inválida (justificando o motivo):
   * Expressão A: {[()]}
   * Expressão B: ([)]
   * Expressão C: ((())
Resolução do Exercício 1
 * 1. Rastreio da Pilha:
   * Início: [ ] (topo = 0)
   * empilhar(10): [10] (topo = 1)
   * empilhar(20): [10, 20] (topo = 2)
   * desempilhar() -> remove 20: [10] (topo = 1)
   * empilhar(30): [10, 30] (topo = 2)
   * empilhar(40): [10, 30, 40] (topo = 3)
   * desempilhar() -> remove 40: [10, 30] (topo = 2)
 * 2. Balanceamento:
   * Expressão A ({[()]}): Válida. Cada símbolo de fechamento encontra seu par correspondente no topo da pilha, e a pilha termina vazia.
   * Expressão B (([)]): Inválida. Ao ler ), o topo da pilha é [ (não é ().
   * Expressão C (((())): Inválida. Ao final da leitura, ainda sobram elementos (() na pilha.
Exercício 2 — Implementação de Pilha com Crescimento Dinâmico em C
Usando a estrutura abaixo, implemente as funções criarPilha, empilhar (dobrando a capacidade com realloc quando topo == cap) e desempilhar (retornando 0 em caso de pilha vazia ou falha de alocação, e 1 em caso de sucesso):
typedef struct {
    int *dados;
    int topo;
    int cap;
} Pilha;

Resolução do Exercício 2
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *dados;
    int topo;
    int cap;
} Pilha;

int criarPilha(Pilha *p, int cap) {
    p->dados = malloc(cap * sizeof(int));
    if (p->dados == NULL) return 0;
    p->topo = 0;
    p->cap = cap;
    return 1;
}

int empilhar(Pilha *p, int x) {
    if (p->topo == p->cap) {
        int nova = 2 * p->cap;
        int *tmp = realloc(p->dados, nova * sizeof(int));
        if (tmp == NULL) return 0; // Mantém p->dados intacto se falhar
        p->dados = tmp;
        p->cap = nova;
    }
    p->dados[p->topo] = x;
    p->topo++;
    return 1;
}

int desempilhar(Pilha *p, int *x) {
    if (p->topo == 0) return 0; // Underflow: pilha vazia
    p->topo--;
    *x = p->dados[p->topo];
    return 1;
}

Exercício 3 — Rastreio de Fila Circular (cap = 4)
Dada uma fila circular com cap = 4, inicialmente vazia (inicio = 0, n = 0), onde o índice de inserção é (inicio + n) % cap e o avanço de inicio é (inicio + 1) % cap:
Execute a sequência:
 * enfileirar(10)
 * enfileirar(20)
 * enfileirar(30)
 * desenfileirar()
 * enfileirar(40)
 * enfileirar(50)
Indique, ao final de cada passo, os valores de inicio, n, o índice acessado/calculado e o elemento removido (quando houver desenfileirar).
Resolução do Exercício 3
 * enfileirar(10): inicio = 0, n = 1, posição (0 + 0) % 4 = 0 -> grava 10.
 * enfileirar(20): inicio = 0, n = 2, posição (0 + 1) % 4 = 1 -> grava 20.
 * enfileirar(30): inicio = 0, n = 3, posição (0 + 2) % 4 = 2 -> grava 30.
 * desenfileirar(): remove 10 da posição 0; inicio passa para (0 + 1) % 4 = 1, n = 2.
 * enfileirar(40): inicio = 1, n = 3, posição (1 + 2) % 4 = 3 -> grava 40.
 * enfileirar(50): inicio = 1, n = 4, posição (1 + 3) % 4 = 0 (volta circular pelo %) -> grava 50. Fila agora está cheia (n == cap).
Exercício 4 — Fila Circular em C e Impressão em Ordem
Implemente enfileirar, desenfileirar e imprimirFila para a estrutura de fila circular abaixo:
typedef struct {
    int *dados;
    int inicio;
    int n;
    int cap;
} Fila;

Resolução do Exercício 4
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *dados;
    int inicio;
    int n;
    int cap;
} Fila;

int enfileirar(Fila *f, int x) {
    if (f->n == f->cap) return 0; // Fila cheia
    int fim = (f->inicio + f->n) % f->cap;
    f->dados[fim] = x;
    f->n++;
    return 1;
}

int desenfileirar(Fila *f, int *x) {
    if (f->n == 0) return 0; // Fila vazia
    *x = f->dados[f->inicio];
    f->inicio = (f->inicio + 1) % f->cap;
    f->n--;
    return 1;
}

void imprimirFila(Fila *f) {
    for (int i = 0; i < f->n; i++) {
        int idx = (f->inicio + i) % f->cap;
        printf("%d ", f->dados[idx]);
    }
    printf("\n");
}

Checklist rápido antes da prova
 * Não altere a struct por valor: sempre receba Pilha *p ou Fila *f quando a função modificar topo, inicio, n, cap ou dados.
 * Topo da pilha: topo guarda a próxima posição livre e o total de elementos; o último elemento inserido está em dados[topo - 1].
 * Ordem na calculadora pós-fixa: ao desempilhar dois operandos para a op b, desempilha-se primeiro b (direito) e depois a (esquerdo).
Quer testar resolver algum desses exercícios passo a passo antes da prova ou simular um problema completo de fila com struct (como o atendimento por senha)?

=============================================================================

Simular um problema completo de Fila Circular com struct é uma excelente estratégia para a avaliação, já que o material da Aula 06 traz exatamente esse formato de questão (como o exercício de atendimento de pacientes com senha e nome) e exige atenção a detalhes práticos de C como inicio, n, cap, operador %, passagem por ponteiro (FilaPac *f) e liberação de memória com free.
Enunciado Simulado — Sistema de Atendimento por Senha (FilaPac)
Você deve implementar em C o controle de uma fila circular de atendimento para pacientes, com capacidade fixa definida ao criar a estrutura (por exemplo, cap = 5):
 * Definição das structs:
   * Paciente: campos int senha e char nome[50].
   * FilaPac: campos Paciente *dados, int inicio, int n e int cap.
 * Funções obrigatórias:
   * int criarFila(FilaPac *f, int cap): aloca dados com malloc, inicializa inicio = 0, n = 0 e cap, retornando 1 em caso de sucesso ou 0 se falhar.
   * int enfileirar(FilaPac *f, Paciente p): se f->n == f->cap, recusa e retorna 0 (fila cheia); caso contrário, insere na posição (f->inicio + f->n) % f->cap e incrementa f->n.
   * int desenfileirar(FilaPac *f, Paciente *removido): se f->n == 0, retorna 0 (fila vazia); caso contrário, copia o elemento em f->inicio para *removido, atualiza f->inicio = (f->inicio + 1) % f->cap e decrementa f->n.
   * void mostrarFila(const FilaPac *f): exibe todos os pacientes na ordem de atendimento (começando em f->inicio, não em 0), usando (f->inicio + i) % f->cap para i de 0 até f->n - 1.
   * void destruirFila(FilaPac *f): libera f->dados com free e zera os campos de controle.
 * Menu em main():
   * 1 — Chegada de paciente (gera a próxima senha sequencial, lê o nome e tenta enfileirar).
   * 2 — Chamar próximo paciente (desenfileira e exibe senha e nome; avisa se estiver vazia).
   * 3 — Mostrar fila em ordem.
   * 0 — Sair, liberando a memória.
Solução Completa em C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int senha;
    char nome[50];
} Paciente;

typedef struct {
    Paciente *dados;
    int inicio;
    int n;
    int cap;
} FilaPac;

int criarFila(FilaPac *f, int cap) {
    f->dados = malloc((size_t)cap * sizeof(Paciente));
    if (f->dados == NULL) {
        return 0;
    }
    f->inicio = 0;
    f->n = 0;
    f->cap = cap;
    return 1;
}

int enfileirar(FilaPac *f, Paciente p) {
    if (f->n == f->cap) {
        return 0; // Fila cheia
    }
    int idx = (f->inicio + f->n) % f->cap;
    f->dados[idx] = p;
    f->n++;
    return 1;
}

int desenfileirar(FilaPac *f, Paciente *removido) {
    if (f->n == 0) {
        return 0; // Fila vazia
    }
    *removido = f->dados[f->inicio];
    f->inicio = (f->inicio + 1) % f->cap;
    f->n--;
    return 1;
}

void mostrarFila(const FilaPac *f) {
    if (f->n == 0) {
        printf("Fila vazia.\n");
        return;
    }
    printf("--- Fila de atendimento (ordem FIFO) ---\n");
    for (int i = 0; i < f->n; i++) {
        int idx = (f->inicio + i) % f->cap;
        printf("%d. Senha #%d - %s\n", i + 1, f->dados[idx].senha, f->dados[idx].nome);
    }
}

void destruirFila(FilaPac *f) {
    free(f->dados);
    f->dados = NULL;
    f->inicio = 0;
    f->n = 0;
    f->cap = 0;
}

int main() {
    FilaPac fila;
    int cap = 5;
    int proximaSenha = 1;
    int opcao;

    if (!criarFila(&fila, cap)) {
        printf("Erro ao alocar memoria para a fila.\n");
        return 1;
    }

    do {
        printf("\n1 - Chegada de paciente\n");
        printf("2 - Chamar proximo\n");
        printf("3 - Mostrar fila em ordem\n");
        printf("0 - Sair\n");
        printf("Escolha: ");
        if (scanf("%d", &opcao) != 1) {
            break;
        }

        if (opcao == 1) {
            if (fila.n == fila.cap) {
                printf("Fila cheia! Nao e possivel cadastrar novo paciente.\n");
            } else {
                Paciente novo;
                novo.senha = proximaSenha;
                printf("Nome do paciente: ");
                scanf(" %49[^\n]", novo.nome);
                if (enfileirar(&fila, novo)) {
                    printf("Paciente '%s' cadastrado com senha #%d.\n", novo.nome, novo.senha);
                    proximaSenha++;
                }
            }
        } else if (opcao == 2) {
            Paciente atendido;
            if (desenfileirar(&fila, &atendido)) {
                printf("Chamando -> Senha #%d: %s\n", atendido.senha, atendido.nome);
            } else {
                printf("Fila vazia! Nenhum paciente para chamar.\n");
            }
        } else if (opcao == 3) {
            mostrarFila(&fila);
        } else if (opcao == 0) {
            destruirFila(&fila);
            printf("Memoria liberada. Encerrando...\n");
        } else {
            printf("Opcao invalida.\n");
        }
    } while (opcao != 0);

    return 0;
}

Pontos de Atenção que Costumam Derrubar na Prova
 * Passagem por ponteiro: criarFila, enfileirar, desenfileirar e destruirFila recebem FilaPac *f porque alteram campos da struct (inicio, n, cap ou dados), enquanto mostrarFila apenas lê os dados.
 * Cópia de Paciente: como Paciente é uma struct simples com int e char[50], atribuir f->dados[idx] = p; ou *removido = f->dados[f->inicio]; copia todos os campos de uma vez.
 * Percurso circular: mostrarFila percorre i de 0 até f->n - 1 e calcula (f->inicio + i) % f->cap para respeitar a volta no vetor sem deslocar elementos.
 * Sem ambiguidade entre vazia e cheia: usar n (f->n == 0 para vazia e f->n == f->cap para cheia) evita o problema clássico de não saber diferenciar fila cheia de vazia apenas com inicio e fim.
Você quer fazer um teste de mesa com uma sequência de chegadas e chamadas nessa FilaPac para praticar os valores de inicio e n?
