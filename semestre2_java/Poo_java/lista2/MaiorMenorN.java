package lista2;
import java.util.Scanner;
public class MaiorMenorN {
    /* Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles.
       A quantidade de números a serem lidos deve será fornecida pelo usuário. */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe a quantidade de números que deseja inserir: ");
        int quantidade = scanner.nextInt();

        if (quantidade <= 0) {
            System.out.println("Quantidade inválida! Digite um número maior que 0.");
        } else {
            System.out.print("Digite o 1º número: ");
            int numero = scanner.nextInt();
            int menor = numero;
            int maior = numero;

            for (int item = 2; item <= quantidade; item++) {
                System.out.print("Digite o " + item + "º número: ");
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
        }

        scanner.close();
    }
}
