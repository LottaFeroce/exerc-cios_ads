package lista2;
import java.util.Scanner;
public class vetor_dez_posicoes_em {
    /*Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba
um novo valor do usuário e verifique se este valor se encontra no vetor. */
public static void main(String[] args) {
        Scanner vetor_dez = new Scanner(System.in);
        int[] vetor = new int[10];

        for (int item = 0; item < 10; item++) {
            System.out.print("Digite o número da posição " + item + ": ");
            vetor[item] = vetor_dez.nextInt();
        }

        System.out.print("Digite um valor para buscar: ");
        int valor = vetor_dez.nextInt();

        boolean encontrado = false;
        for (int n : vetor) {
            if (n == valor) {
                encontrado = true;
                break;
            }
        }

        if (encontrado) {
            System.out.println("O valor " + valor + " está no vetor!");
        } else {
            System.out.println("O valor " + valor + " não foi encontrado.");
        }
        vetor_dez.close();
    }
}