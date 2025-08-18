package lista2;
import java.util.Scanner;
public class bola_quadrada_e_raiz_em {
    /*Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e esreva
para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados
com um valor negativo ou zero. */
     public static void main(String[] args) {
        Scanner Fig_tart = new Scanner(System.in);
        double num;

        while (true) {
            System.out.print("Digite um número (0 ou negativo para parar): ");
            num = Fig_tart.nextDouble();
            if (num <= 0) break;

            System.out.println("Número: " + num);
            System.out.println("Quadrado: " + (num * num));
            System.out.println("Cubo: " + (num * num * num));
            System.out.println("Raiz quadrada: " + Math.sqrt(num));
        }
        Fig_tart.close();
    }
}