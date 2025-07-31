package lista1;
import java.util.Scanner;
public class SomAlgarismos {
/*
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
o número lido não for maior do que zero, o programa termina com a mensagem “Número
inválido”. */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro maior que zero: ");
        int numero = scanner.nextInt();
        if (numero <= 0) {
            System.out.println("Número inválido");
        } else {
            int soma = 0;
            int temporario = numero;

            while (temporario > 0) {
                soma += temporario % 10;  
                temporario /= 10;         
            }
            System.out.println("A soma dos algarismos de " + numero + " é: " + soma);
        }
        scanner.close();
    }
}
