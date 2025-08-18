package lista2;
import java.util.Scanner;
public class inteiros_ate_um_negativo_em {
    /*Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
negativo. O programa tem que retornar o maior e o menor número lido */
 public static void main(String[] args) {
        Scanner Spiral_staircase = new Scanner(System.in);
        int num, maior = Integer.MIN_VALUE, menor = Integer.MAX_VALUE;

        while (true) {
            System.out.print("Digite um número (negativo para parar): ");
            num = Spiral_staircase.nextInt();
            if (num < 0) break;

            if (num > maior) maior = num;
            if (num < menor) menor = num;
        }

        if (maior != Integer.MIN_VALUE) {
            System.out.println("Maior número: " + maior);
            System.out.println("Menor número: " + menor);
        } else {
            System.out.println("Nenhum número válido informado.");
        }
        Spiral_staircase.close();
    }
}