package lista2;
import java.util.Scanner;
public class dez_numeros_maior_em {
    /* Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido. exerc: [9]*/
    public static void main(String[] args) {
        Scanner mesmo_exerc_5_vezese_seguidas = new Scanner(System.in);
        int menor, maior;
        System.out.print("Digite o 1º número: ");
        int numero = mesmo_exerc_5_vezese_seguidas.nextInt();
        menor = maior = numero;
        for (int item = 2; item <= 10; item++) {
            System.out.print("Digite o " + item + "º número: ");
            numero = mesmo_exerc_5_vezese_seguidas.nextInt();
            if (numero < menor) {
                menor = numero;
            }
            if (numero > maior) {
                maior = numero;
            }
        }
        System.out.println("Menor número lido: " + menor);
        System.out.println("Maior número lido: " + maior);
        mesmo_exerc_5_vezese_seguidas.close();
    }
}
