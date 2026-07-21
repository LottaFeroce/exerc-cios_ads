#include <stdio.h>

int main() {
    float distancia, tempo, velocidade;

    printf("Digite a distancia (m): ");
    scanf("%f", &distancia);

    printf("Digite o tempo (s): ");
    scanf("%f", &tempo);

    velocidade = distancia / tempo;

    printf("Velocidade = %.2f m/s\n", velocidade);

    return 0;
}