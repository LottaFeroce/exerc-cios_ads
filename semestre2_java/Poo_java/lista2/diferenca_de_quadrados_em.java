package lista2;
public class diferenca_de_quadrados_em {
    /*Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100
números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números
naturais e,
12 + 22 + ... + 102 = 385
• quadrado da soma dos dez primeiros números naturais é,
(1 + 2 + ... + 10)2 = 552 = 3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da
soma e 3025-385 = 2640.  */
     public static void main(String[] args) {
        int soma_quadrados = 0;
        int soma = 0;

        for (int item = 1; item <= 100; item++) {
            soma_quadrados += item * item;
            soma += item;
        }

        int quadrado_da_soma = soma * soma;
        int diferenca = quadrado_da_soma - soma_quadrados;

        System.out.println("Diferença = " + diferenca);
    }
}