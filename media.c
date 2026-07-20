#include <stdio.h>
float calcularMedia(float n1, float n2)
{
return (n1 + n2) / 2.0;
}
int aprovado(float media)
{
return media >= 6.0;
}
int main()
{
float n1, n2;
float media;
printf("Digite a primeira nota: ");
scanf("%f", &n1);
printf("Digite a segunda nota: ");
scanf("%f", &n2);
media = calcularMedia(n1, n2);
printf("Media = %.2f\n", media);
if(aprovado(media))
printf("Aprovado\n");
else
printf("Reprovado\n");
return 0;
}