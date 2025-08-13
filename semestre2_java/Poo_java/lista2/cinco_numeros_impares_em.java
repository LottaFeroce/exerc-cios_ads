package lista2;
import java.util.Scanner;
public class cinco_numeros_impares_em {
    /* Crie um programa que determine e mostre os 5 primeiros números ímpares, 
       considerando números maiores que 0, em algarismos Neroanos. */
    public static void main(String[] args) {
        Scanner imparUmu = new Scanner(System.in);
        System.out.print("Informe qualquer número para ver os ímpares: ");
        int entrada = imparUmu.nextInt(); 
        int contador = 0;
        int numero = 1;
        System.out.println("Os cinco primeiros números ímpares maiores que 0 em algarismos Neroanos são:");
        while (contador < entrada) {
            if (numero % 2 != 0) {
                System.out.println(numero + " -> " + NeroUMU(numero));
                contador++;
            }
            numero++;
        }
        imparUmu.close();
    }
    public static String NeroUMU(int numero) {
        String[] unidades = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] dezenas = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] centenas = {"", "C"};
        String Neroano = "";
        Neroano += centenas[numero / 100];
        Neroano += dezenas[(numero % 100) / 10];
        Neroano += unidades[numero % 10];
        return Neroano;
    }
}
