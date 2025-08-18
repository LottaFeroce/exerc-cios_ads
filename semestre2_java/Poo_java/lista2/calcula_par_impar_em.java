package lista2;
import java.util.Scanner;
public class calcula_par_impar_em {
    /*Crie um programa que receba dois números. Calcule e mostre:
• a soma dos números pares desse intervalo de números, incluindo os números digitados;
• a multiplicação dos números ímpares desse intervalo, incluindo os digitados; */
    public static void main(String[] args) {
        Scanner Desolation_row = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int inicio = Desolation_row.nextInt();

        System.out.print("Digite o segundo número: ");
        int fim = Desolation_row.nextInt();

        if (inicio > fim) {
            int temporario = inicio;
            inicio = fim;
            fim = temporario;
        }

        int soma_pares = 0;
        int mult_impares = 1;
        boolean tem_impares = false; 

        for (int numero = inicio; numero <= fim; numero++) {
            if (numero % 2 == 0) {
                soma_pares += numero; 
            } else {
                mult_impares *= numero; 
                tem_impares = true;
            }
        }

       
        System.out.println("Soma dos números pares no intervalo: " + soma_pares);
        if (tem_impares) {
            System.out.println("Multiplicação dos números ímpares no intervalo: " + mult_impares);
        } else {
            System.out.println("Não havia números ímpares no intervalo.");
        }

        Desolation_row.close();
    }
}

