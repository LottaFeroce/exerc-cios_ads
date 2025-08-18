package lista2;

public class valor_de_S_em {
    /*. Escreva um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + ...99/50 */
    public static void main(String[] args) {
        double valor_s = 0;
        int numerador = 1;

        for (int denominador = 1; denominador <= 50; denominador++) {
            valor_s += (double) numerador / denominador;
            numerador += 2; 
        }

        System.out.println("Valor de S = " + valor_s);
    }
}