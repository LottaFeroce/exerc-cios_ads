package lista2;
import java.util.Scanner;
public class soma_de_dez_numeros_em {
    /* Escreva um programa que peça ao usuário para digitar 10 valores e some-os. */
    public static void main(String[] args) {
        System.out.println("Informe dez valores para receber a soma dos mesmos: "); 
        Scanner pseudocalc = new Scanner(System.in);
        Float soma = 0f;
        Integer counter = 0;     
        while (counter < 10) {
            System.out.print("Digite o " + (counter + 1) + "º valor: ");
            Float numero = pseudocalc.nextFloat(); 
            soma += numero; 
            counter++; 
        } 
        System.out.println("A soma dos 10 valores informados é: " + soma);   
        pseudocalc.close();
    }
}
