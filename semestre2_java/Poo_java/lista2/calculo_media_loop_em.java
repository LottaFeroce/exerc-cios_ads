package lista2;
import java.util.Scanner;
public class calculo_media_loop_em {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double soma = 0;
        int count = 0;

        while (true) {
            System.out.print("Digite a nota (0 a 10): ");
            double nota = sc.nextDouble();

            if (nota < 0 || nota > 10) break;

            soma += nota;
            count++;
        }

        if (count > 0) {
            System.out.println("Média = " + (soma / count));
        } else {
            System.out.println("Nenhuma nota válida informada.");
        }
        sc.close();
    }
}
