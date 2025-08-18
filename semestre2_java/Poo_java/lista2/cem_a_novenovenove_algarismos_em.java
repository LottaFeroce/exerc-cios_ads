package lista2;
import java.util.Scanner;
public class cem_a_novenovenove_algarismos_em {
    /*Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um
dos algarismos que compõem o número. */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número entre 100 e 9999: ");
        int numero = scanner.nextInt();

        if (numero < 100 || numero > 9999) {
            System.out.println("Número inválido! Digite um valor entre 100 e 9999.");
        } else {
            System.out.println("Algarismos:");
            while (numero > 0) {
                int algarismo = numero % 10;  
                numero /= 10;                
                
                System.out.println(algarismo);
            }
        }

        scanner.close();
    }
}