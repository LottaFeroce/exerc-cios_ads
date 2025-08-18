package lista2;
import java.util.Scanner;
public class somatoria_de_cinco_numeros_em {
    /*Ercreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório
desses números na tela. Após exibir a soma, o programa deve mostrar também os números que
o usuário digitou, um por linha. */
   public static void main(String[] args) {
        Scanner somatoria_socorro = new Scanner(System.in);
        int[] numeros = new int[5];
        int soma = 0;

        for (int item = 0; item < 5; item++) {
            System.out.print("Digite o número " + (item+1) + ": ");
            numeros[item] = somatoria_socorro.nextInt();
            soma += numeros[item];
        }

        System.out.println("Soma = " + soma);
        System.out.println("Números digitados:");
        for (int n : numeros) {
            System.out.println(n);
        }
        somatoria_socorro.close();
    }
}