package lista2;
import java.util.Scanner;
public class pares_positivos_n_decrescente_em {
    /*Crie um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem decrescente. [14]*/
    public static void main(String[] args) {
        Scanner par_dnv = new Scanner(System.in);
        System.out.print("Informe um número inteiro positivo par: ");
        int entrada = par_dnv.nextInt();
            if (entrada < 0 || entrada % 2 != 0) {
                System.out.println("Número inválido! Digite apenas um inteiro positivo par.");
            } else {
                System.out.printf("Números pares de %d até 0:\n", entrada);
                int item = entrada;
                while (item >= 0) {
                    System.out.println(item + " -> Par");
                    item -= 2;
                }
        }
        par_dnv.close();
    }
}
