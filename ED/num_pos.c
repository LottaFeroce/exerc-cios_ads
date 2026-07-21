#include <stdio.h>

int main() {
    int numero;

    printf("Digite um numero inteiro: ");
    scanf("%d", &numero);

    if (numero > 0)
        printf("Positivo\n");
    else if (numero < 0)
        printf("Negativo\n");
    else
        printf("Nulo\n");

    return 0;
}