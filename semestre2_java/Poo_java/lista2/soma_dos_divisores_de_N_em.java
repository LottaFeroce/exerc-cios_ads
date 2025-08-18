package lista2;
import java.util.Scanner;
public class soma_dos_divisores_de_N_em {
 public static void main(String[] args) {
        Scanner seven = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        int n = seven.nextInt();
        int soma = 0;

        for (int item = 1; item < n; item++) {
            if (n % item == 0) soma += item;
        }

        System.out.println("Soma dos divisores: " + soma);
        seven.close();
    }
}