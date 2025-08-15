package lista2;
import java.util.Scanner;

public class PositivosMediaEm {
    /* Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média. */
    public static void main(String[] args) {
        System.out.println("Informe dez valores positivos para calcular a soma e a média dos mesmos: ");
        Scanner pseudocalc = new Scanner(System.in);
        double soma = 0; 
        int counter = 0;  
        while (counter < 10) {
            System.out.print("Digite o " + (counter + 1) + "º valor: ");
            double numero = pseudocalc.nextDouble();  
            if (numero > 0) {
                soma += numero;
                counter++;  
            } else {
                System.out.println("Valor inválido. Digite um número positivo.");
            }
        }
        double media = soma / 10;
        System.out.println("A soma dos 10 valores positivos informados é: " + soma + " e a média foi: " + media);
        pseudocalc.close();
    }
}
