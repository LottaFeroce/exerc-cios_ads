package lista2;
import java.util.Scanner;
public class numeros_naturais_crescnt_em {
    /* Crie um programa que leia um número inteiro positivo N 
       e imprima todos os números naturais de 0 até N em ordem crescente. [12] */
    public static void main(String[] args) {
        Scanner mesmo_exercicio_que_o_numero10 = new Scanner(System.in);
        System.out.print("Informe qualquer número contanto que seja natural: ");
        int entrada = mesmo_exercicio_que_o_numero10.nextInt(); 
        if (entrada < 0) {
            System.out.println("Número inválido! Digite apenas números naturais (0 ou positivos).");
        } else {
            System.out.printf("Os números naturais de 0 até %d são:\n", entrada);
            for (int item = 0; item <= entrada; item++) {
                System.out.println(item + " -> Natural");
            }
        }
        mesmo_exercicio_que_o_numero10.close();
    }
}
