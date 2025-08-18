package lista2;
import java.util.Scanner;
public class media_dez_alunos_em {
    /* Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.  */
    public static void main(String[] args) {
        Scanner mediante_ao_julgamento_divino_eles_tremeram = new Scanner(System.in);
        double[] medias = new double[10];
        int aprovados = 0;

        for (int item = 0; item < 10; item++) {
            double soma = 0;
            System.out.println("Notas do aluno " + (item+1) + ":");
            for (int jtem = 0; jtem < 4; jtem++) {
                System.out.print("Nota " + (jtem+1) + ": ");
                soma += mediante_ao_julgamento_divino_eles_tremeram.nextDouble();
            }
            medias[item] = soma / 4;
            if (medias[item] >= 7.0) aprovados++;
        }

        System.out.println("Número de alunos com média >= 7.0: " + aprovados);
        mediante_ao_julgamento_divino_eles_tremeram.close();
    }
}