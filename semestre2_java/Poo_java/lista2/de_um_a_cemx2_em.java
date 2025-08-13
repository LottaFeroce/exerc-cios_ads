package lista2;
import java.util.Scanner;
public class de_um_a_cemx2_em {
    /* Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes.
       A primeira vez deve usar a estrutura de repetição for e a segunda while. */
    public static void main(String[] args) {
        Scanner numeralscorpse = new Scanner(System.in);
        System.out.print("Informe qualquer número para começar a contagem até 100! Wow!!!: ");
        Integer entrada = numeralscorpse.nextInt();
        System.out.println("\nContagem de 1 a 100 usando FOR:");
        for (int item = entrada; item <= 100; item++) {
            System.out.print(item + " ");
        }
        System.out.println("\n\nContagem de 1 a 100 usando WHILE:");
        int jtem = entrada;
        while (jtem <= 100) {
            System.out.print(jtem + " ");
            jtem++;
        }
        System.out.println("\n\nFim da contagem!");
        numeralscorpse.close();
    }
}
