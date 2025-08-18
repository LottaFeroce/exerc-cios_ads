package lista2;
import java.util.Scanner;
import java.util.Random;
public class adivinha_quem_e_em {
    /*Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar acertar qual
o número foi gerado, a cada tentativa o programa deverá informar se o chute e menor ou maior
que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa
deve informar em quantas tentativas o número foi descoberto.  */
    public static void main(String[] args) {
        Scanner Rhinoceros_beetle = new Scanner(System.in);
        Random rand = new Random();

        int numero_secreto = rand.nextInt(100) + 1;
        int tentativas = 0;
        int chute;

        do {
            System.out.print("Digite seu chute (1 a 100): ");
            chute = Rhinoceros_beetle.nextInt();
            tentativas++;

            if (chute < numero_secreto) {
                System.out.println("O número é maior!");
            } else if (chute > numero_secreto) {
                System.out.println("O número é menor!");
            } else {
                System.out.printf("Parabéns! Você acertou em %d tentativas!",tentativas);
            }
        } while (chute != numero_secreto);

        Rhinoceros_beetle.close();
    }
}