package lista2;
import java.util.Scanner;
public class n_numeros_inteiros_para_n_primos_em {
    /*Esreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros
números primos.  */
    public static void main(String[] args) {
        Scanner Spiral_staircase = new Scanner(System.in);
        System.out.print("Digite o valor de n: ");
        int numero = Spiral_staircase.nextInt();
        
        int soma = 0;
        int count = 0;
        int num = 2;

        while (count < numero) {
            boolean numero_primo = true; 

           
            for (int item = 2; item <= Math.sqrt(num); item++) {
                if (num % item == 0) {
                    numero_primo = false; 
                    break;  
                }
            }

            if (numero_primo) {
                soma += num;
                count++;
            }
            num++;
        }

        System.out.printf("Soma dos %d primeiros números primos = %d",numero, soma);
        Spiral_staircase.close();
    }
}
