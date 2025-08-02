package lista1;
import java.util.Scanner;
public class loja_tintas_em {
/* Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;*/
    public static void main(String[] args) {
        Scanner tintas = new Scanner(System.in);
        System.out.print("Informe o tamanho da área a ser pintada (em m²): ");
            double area = tintas.nextDouble();
            double litros_necessarios = area / 6.0;
            int latas18 = (int) Math.ceil(litros_necessarios / 18.0);
            double precos_latas = latas18 * 80.0;
            int galoes36 = (int) Math.ceil(litros_necessarios / 3.6);
            double precos_galoes = galoes36 * 25.0;
            System.out.println("\nOpção 1: Apenas latas de 18 litros");
            System.out.println("Quantidade de latas: " + latas18);
            System.out.printf("Preço total: R$ %.2f%n", precos_latas);
            System.out.println("\nOpção 2: Apenas galões de 3,6 litros");
            System.out.println("Quantidade de galões: " + galoes36);
            System.out.printf("Preço total: R$ %.2f%n", precos_galoes);
        tintas.close();
    }
}
