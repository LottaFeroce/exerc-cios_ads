package lista1;
import java.util.Scanner;
public class raiz4 {
    public static void main(String[] args) {
        Scanner raizq = new Scanner(System.in);
            System.out.println("Informe um valor positivo para que seja calculada sua raiz: ");
            double Raiz = raizq.nextDouble();
            System.out.printf("A raiz de %.1f é: %.1f%n", Raiz, Math.sqrt(Raiz));
            if (Raiz <0){
                System.out.println("Valor inválido");
            }
        raizq.close();
    }
    
}
