package lista1;
import java.util.Scanner;
public class trapezio_decendente_birr {
/*Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:
Lembre-se a base maior e a base menor devem ser números maiores que zero */
    public static void main(String[] args) {
        Scanner trapez = new Scanner(System.in);
        System.out.println("Informe as bases e a altura do trapézio:");
            double base_menor = trapez.nextDouble();
            double base_maior = trapez.nextDouble();
            double altura = trapez.nextDouble();
            if (base_menor > 0 && base_maior > 0 && altura > 0) {
                double area = (base_menor + base_maior) * altura / 2;
                System.out.printf("A área do trapézio é: %.2f%n", area);
            } else {
                System.out.println("Valores inválidos! As bases e a altura devem ser maiores que zero.");
            }
        trapez.close();
    }
}
