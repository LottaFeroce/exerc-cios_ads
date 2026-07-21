#include <stdio.h>

int main() {
    int a, b;

    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &a, &b);

    printf("Soma = %d\n", a + b);
    printf("Diferenca = %d\n", a - b);
    printf("Produto = %d\n", a * b);
    printf("Resto = %d\n", a % b);

    return 0;
}