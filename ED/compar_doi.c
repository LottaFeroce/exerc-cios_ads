#include <stdio.h>

int main() {
    int a, b;

    printf("Digite dois numeros: ");
    scanf("%d %d", &a, &b);

    printf("A > B? %d\n", a > b);
    printf("B > A? %d\n", b > a);
    printf("A == B? %d\n", a == b);
/*operador ternario int maior = (a>b)?a:b;*/
    return 0;
}