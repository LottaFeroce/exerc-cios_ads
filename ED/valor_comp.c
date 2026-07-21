#include <stdio.h>

int main() {
    float valor, total;
    int tipo;

    printf("Digite o valor da compra: ");
    scanf("%f", &valor);

    printf("Digite o tipo do produto: ");
    scanf("%d", &tipo);

    if (tipo == 0)
        total = valor * 1.10;
    else
        total = valor * 1.20;

    printf("Valor total: R$ %.2f\n", total);

    return 0;
}