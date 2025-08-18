package lista2;
public class soma_de_naturais_abaixo_de_mil_em {
    /*Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3
ou 5. */
public static void main(String[] args) {
        int soma = 0;
        for (int item = 1; item < 1000; item++) {
            if (item % 3 == 0 || item % 5 == 0) soma += item;
        }
        System.out.println("Soma = " + soma);
    }
}