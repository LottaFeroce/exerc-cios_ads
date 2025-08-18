package lista2;
import java.util.Scanner;
public class calculo_de_associacao_em_paralelo_em {
    /*Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos
pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
entre com um valor para resistência igual a zero.  */
    public static void main(String[] args) {
        Scanner Desolation_row = new Scanner(System.in);
        double r1, r2;

        while (true) {
            System.out.print("Digite R1 (0 para parar): ");
            r1 = Desolation_row.nextDouble();
            if (r1 == 0) break;

            System.out.print("Digite R2 (0 para parar): ");
            r2 = Desolation_row.nextDouble();
            if (r2 == 0) break;

            double rp = (r1 * r2) / (r1 + r2);
            System.out.println("Resistência equivalente em paralelo: " + rp);
        }
        Desolation_row.close();
    }
}