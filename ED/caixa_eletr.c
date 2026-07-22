#include <stdio.h>

int main() {
    float saldo = 0.0;
    int operacao;
    float valor;

    do {
        printf("\n===============================\nInforme qual operação você quer executar:\n1 - Consultar Saldo\n2 - Depositar\n3 - Sacar\n4 - Sair\n===============================\nOpcão: ");
        scanf("%d", &operacao);

        if (operacao == 1) {
            printf("Seu saldo atual é: R$ %.2f\n", saldo);
        } 
        else if (operacao == 2) {
            printf("Informe o valor para deposito: ");
            scanf("%f", &valor);
            if (valor > 0) {
                saldo += valor;
                printf("Deposito de R$ %.2f realizado com sucesso!\n", valor);
            } else {
                printf("Valor invalido. Deposite um valor positivo.\n");
            }
        } 
        else if (operacao == 3) {
            printf("Informe o valor para saque: ");
            scanf("%f", &valor);
            if (valor > 0 && valor <= saldo) {
                saldo -= valor;
                printf("Saque de R$ %.2f realizado com sucesso!\n", valor);
            } else if (valor > saldo) {
                printf("Saldo insuficiente para realizar o saque.\n");
            } else {
                printf("Valor invalido. Informe um valor positivo.\n");
            }
        } 
        else if (operacao == 4) {
            printf("Saindo do sistema\n");
        } 
        else {
            printf("Opção invalida! Tente novamente.\n");
        }

    } while (operacao != 4);

    return 0;
}