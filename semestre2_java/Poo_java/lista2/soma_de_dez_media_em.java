package lista2;
import java.util.Scanner;
public class soma_de_dez_media_em {
    /* Escreva um programa que leia 10 inteiros e imprima sua média. */
    public static void main(String[] args) {
        System.out.println("Informe dez valores para receber a soma e a média dos mesmos: "); 
        Scanner pseudocalc = new Scanner(System.in);
        double soma = 0; 
        Integer counter = 0;  
        while (counter < 10) {
            System.out.print("Digite o " + (counter + 1) + "º valor: ");
            double numero = pseudocalc.nextDouble();  
            soma += numero;  
            counter++;  
        }
        double media = soma / 10;  
        System.out.println("A soma dos 10 valores informados é: " + soma + " e a média foi: " + media); 
        pseudocalc.close();  
    }
}
