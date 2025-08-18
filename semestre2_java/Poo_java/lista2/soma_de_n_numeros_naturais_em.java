package lista2;
import java.util.Scanner;
public class soma_de_n_numeros_naturais_em {
    /*Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros
números naturais [16]*/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo: ");
        int n = scanner.nextInt();
        if (n < 0) {
            System.out.println("Número inválido! Por favor, digite um inteiro maior ou igual a 0.");
        } else {
            int soma = n * (n + 1) / 2;
            System.out.println("A soma dos " + n + " primeiros números naturais é: " + soma);
        }
        scanner.close();
    }
}
