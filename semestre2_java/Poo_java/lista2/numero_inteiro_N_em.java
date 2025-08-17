package lista2;
import java.util.Scanner;

public class numero_inteiro_N_em {
    /*Crie um programa que leia um número inteiro N e depois imprima os N primeiros números
    naturais ímpares. [10]*/
    
    public static void main(String[] args) {
        Scanner impar_dnv = new Scanner(System.in);
        System.out.print("Informe qualquer número para ver os ímpares: ");
        int entrada = impar_dnv.nextInt(); 
        int contador = 0;
        int numero = 1;
        
        System.out.printf("Os %d primeiros números ímpares maiores que 0 são:\n", entrada);
        
        while (contador < entrada) {
            if (numero % 2 != 0) {
                System.out.println(numero + " -> Ímpar");
                contador++;
            }else{
                System.out.printf("%d <- Par\n",numero);
            }
            numero++;
        }
        
        impar_dnv.close();
    }
}
