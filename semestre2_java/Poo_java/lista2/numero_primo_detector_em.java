package lista2;
import java.util.Scanner;
public class numero_primo_detector_em {
    /*Ecreva um programa que receba um número inteiro maior do que 1, e verifique se o número
fornecido é primo ou não. */
     public static void main(String[] args) {
        Scanner pois_sabiam_que_seus_destinos_estavam_selados = new Scanner(System.in);
        System.out.print("Digite um número inteiro maior que 1: ");
        int numero = pois_sabiam_que_seus_destinos_estavam_selados.nextInt();

        boolean primo = true;
        if (numero <= 1) primo = false;
        else {
            for (int item = 2; item <= Math.sqrt(numero); item++) {
                if (numero % item == 0) {
                    primo = false;
                    break;
                }
            }
        }

        if (primo) System.out.println(numero + " é primo.");
        else System.out.println(numero + " não é primo.");
        pois_sabiam_que_seus_destinos_estavam_selados.close();
    }
}