package lista1;
import java.util.Scanner;
public class raiz_quadrado {
    public static void main(String[] args) {
        Scanner raizq = new Scanner(System.in);

        System.out.println("Informe um valor positivo para que seja calculada sua raiz: ");
        double Raiz = raizq.nextDouble();

        if (Raiz < 0) {
            System.out.println("Valor inválido");
        } else {
            System.out.printf("O número é: %.1f | O quadrado é: %.1f | A raiz é: %.1f%n", 
                              Raiz, Math.pow(Raiz, 2), Math.sqrt(Raiz));
        }

        raizq.close();
    }
}
