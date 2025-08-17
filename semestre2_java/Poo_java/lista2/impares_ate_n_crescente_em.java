package lista2;
import java.util.Scanner;
public class impares_ate_n_crescente_em {
    /*Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os números
ímpares de 1 até N em ordem crescente.  [15]*/
    public static void main(String[] args) {
        Scanner par_dnv = new Scanner(System.in);
        System.out.print("Informe um número inteiro positivo par: ");
        int entrada = par_dnv.nextInt();
        if (entrada < 0 || entrada % 2 == 0) {
            System.out.println("Número inválido! Digite apenas um inteiro positivo ímpar.");
        } else {
            System.out.printf("Números ímpares de 0 até %d:\n", entrada);
            for (int item = 1; item <= entrada; item += 2) {
                System.out.println(item + " -> Ímpar");
            }
        }
        par_dnv.close();
    }
}