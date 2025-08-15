package lista2;
import java.util.Scanner;
public class de_mil_em_mil_em {
    /*Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em
1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).  */
    public static void main(String[] args) {
        System.out.print("Informe um inteiro que seja zero ou igual a zero: ");
        Scanner zeronumero = new Scanner(System.in);
        Integer zero = zeronumero.nextInt();
        if (zero == 0) {
            for (int item = zero; item <= 100000; item+= 1000) {
                System.out.print(item + " ");
            }
            
        }else{
            System.out.println("O valor deve ser zero");
        }
        zeronumero.close();
    } 
}
