package lista2;
import java.util.Scanner;
import java.util.ArrayList;
public class listas_par_impar_em {
    /*Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os
números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.  */
   public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> numeros = new ArrayList<>();
        ArrayList<Integer> pares = new ArrayList<>();
        ArrayList<Integer> impares = new ArrayList<>();

        for (int item = 0; item < 20; item++) {
            System.out.print("Digite o número " + (item+1) + ": ");
            int num = sc.nextInt();
            numeros.add(num);

            if (num % 2 == 0) pares.add(num);
            else impares.add(num);
        }

        System.out.println("Todos: " + numeros);
        System.out.println("Pares: " + pares);
        System.out.println("Ímpares: " + impares);
        sc.close();
    }
}