package lista1;
import java.util.Scanner;
public class brecho {/*brecho caso valor < 50 aumente 45%, caso contrario valor + 30% */
    public static void main(String[] args) {
        Scanner cal = new Scanner(System.in);
        System.out.println("Informe o valor do produto a ser processado: ");
        double val = cal.nextDouble();
        double menor50 = 45.0 / 100.0;  
        double maior50 = 30.0 / 100.0;  

        if (val < 50) {
            System.out.printf("O valor ajustado do produto é: %.2f\n", val + (val * menor50)); 
        } else if (val > 50) {
            System.out.printf("O valor ajustado do produto é: %.2f\n", val + (val * maior50)); 
        } else {
            System.out.println("Valor inválido");
        }

        cal.close();
    }
}
