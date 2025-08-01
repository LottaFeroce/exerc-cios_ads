package lista1;
import java.util.Scanner;
public class calendario_semanal {
    /*
Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.
     */
    public static void main(String[] args) {
        Scanner semana = new Scanner(System.in);
        System.out.print("Digite um número de 1 a 7 para saber o dia da semana: ");
        int dia = semana.nextInt();
        String[] dias = {
            "Domingo", "Segunda-feira", "Terça-feira",
            "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"
        };
        if (dia >= 1 && dia <= 7) {
            System.out.println("Dia correspondente: " + dias[dia - 1]);
        } else {
            System.out.println("Valor inválido! Tente um número de 1 a 7.");
        }
        semana.close();
    }
}
