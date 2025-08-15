package lista2;
import java.util.Scanner;
public class dez_numeros_maior_em {
    /* Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido. exerc: [9]*/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int menor, maior;
        System.out.print("Digite o 1º número: ");
        int numero = scanner.nextInt();
        menor = maior = numero;
        for (int i = 2; i <= 10; i++) {
            System.out.print("Digite o " + i + "º número: ");
            numero = scanner.nextInt();
            if (numero < menor) {
                menor = numero;
            }
            if (numero > maior) {
                maior = numero;
            }
        }
        System.out.println("Menor número lido: " + menor);
        System.out.println("Maior número lido: " + maior);
        scanner.close();
    }
}
