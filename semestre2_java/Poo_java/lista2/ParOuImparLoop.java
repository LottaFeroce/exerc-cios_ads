package lista2;
import java.util.Scanner;
public class ParOuImparLoop {
    /* Ler uma sequência de números inteiros e determinar se eles são pares ou não.
       Deverá ser informado o número de dados lidos e número de valores pares.
       O processo termina quando for digitado o número 0. */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int contador = 0; 
        int pares = 0;    
        int impares = 0;    

        System.out.print("Digite um número inteiro (0 para sair): ");
        int numero = scanner.nextInt();

        while (numero != 0) {
            contador++;

            if (numero % 2 == 0) {
                System.out.println(numero + " <- Par");
                pares++;
            } else {
                System.out.println(numero + " -> Ímpar");
                impares++;
            }

            System.out.print("Digite outro número (0 para sair): ");
            numero = scanner.nextInt();
        }

        System.out.println("\nQuantidade de números lidos: " + contador);
        System.out.printf("Quantidade de números pares: %d\nQuantidade de números ímpares: %d",pares,impares);

        scanner.close();
    }
}
