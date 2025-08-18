package lista2;
import java.util.Scanner;
public class vetor_consoantes_em {
    /*Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.  */
    public static void main(String[] args) {
        Scanner consoantes_vetantes = new Scanner(System.in);
        char[] vetor = new char[10];
        int count = 0;

        System.out.println("Digite 10 caracteres:");
        for (int item = 0; item < 10; item++) {
            vetor[item] = consoantes_vetantes.next().toLowerCase().charAt(0);
        }

        System.out.print("Consoantes lidas: ");
        for (char consoantes : vetor) {
            if (Character.isLetter(consoantes) && !"aeiou".contains(String.valueOf(consoantes))) {
                System.out.print(consoantes + " ");
                count++;
            }
        }

        System.out.println("\nTotal de consoantes: " + count);
        consoantes_vetantes.close();
    }
}