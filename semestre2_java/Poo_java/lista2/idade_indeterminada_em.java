package lista2;
import java.util.Scanner;
public class idade_indeterminada_em {
    /*Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando for
informada a idade 0), e calcule a idade média desse grupo.  */
  public static void main(String[] args) {
        Scanner Rhinoceros_beetle = new Scanner(System.in);
        int idade, soma = 0, count = 0;

        while (true) {
            System.out.print("Digite a idade (0 para parar): ");
            idade = Rhinoceros_beetle.nextInt();
            if (idade == 0) break;
            soma += idade;
            count++;
        }

        if (count > 0) {
            System.out.println("Média de idades: " + (soma / (double) count));
        } else {
            System.out.println("Nenhuma idade informada.");
        }
        Rhinoceros_beetle.close();
    }
}