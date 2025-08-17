package lista2;
import java.util.Scanner;
public class zero_a_cem_soma_pares_em {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite um número inteiro entre 0 e 100: ");
        int limite = entrada.nextInt();
        int soma = 0;
        if (limite < 0 || limite > 100) {
            System.out.println("Número inválido! Digite entre 0 e 100.");
        } else {
            for (int i = 0; i <= limite; i++) {
                if (i % 2 == 0) {
                    soma += i;
                }
            }
            System.out.printf("A soma dos números pares de 0 até %d é: %d%n", limite, soma);
        }
        entrada.close();
    }
}
