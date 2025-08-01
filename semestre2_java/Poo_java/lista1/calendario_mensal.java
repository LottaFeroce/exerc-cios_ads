package lista1;
import java.util.Scanner;
public class calendario_mensal {
/*
Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este
número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.
*/
    public static void main(String[] args) {
        Scanner mensal = new Scanner(System.in);
        System.out.print("Digite um numero de 1 a 12 para saber qual mês é: ");
        int mes = mensal.nextInt();
        String[] meses = {
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho", "Julho",
             "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        };
        if (mes >= 1 && mes <= 12) {
            System.out.println("Mês correspondente: " + meses[mes - 1]);
        } else {
            System.out.println("Valor inválido! Tente um número de 1 a 12.");
        }
        mensal.close();
    }
}
