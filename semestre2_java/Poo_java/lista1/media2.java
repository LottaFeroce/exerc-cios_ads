package lista1;
import java.util.Scanner;

public class media2 {
    public static void main(String[] args) {
        Scanner med = new Scanner(System.in);
        
        System.out.println("Informe duas notas válidas (entre 0.0 e 10.0): ");
        double nota1 = med.nextDouble();
        double nota2 = med.nextDouble();

        if ((nota1 >= 0 && nota1 <= 10) && (nota2 >= 0 && nota2 <= 10)) {
            double media = (nota1 + nota2) / 2;
            System.out.printf("A média do aluno é: %.2f%n", media);
        } else {
            System.out.println("Uma ou ambas as notas são inválidas. Encerrando o programa.");
        }

        med.close();
    }
}
