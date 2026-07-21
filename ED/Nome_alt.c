#include <stdio.h>

int main() {
    char nome[50];
    int idade;
    float altura;

    printf("Digite o nome: ");
    scanf("%49s", nome);

    printf("Digite a idade: ");
    scanf("%d", &idade);

    printf("Digite a altura: ");
    scanf("%f", &altura);

    printf("\nNome: %s\n", nome);
    printf("Idade: %d anos\n", idade);
    printf("Altura: %.2f m\n", altura);

    return 0;
}