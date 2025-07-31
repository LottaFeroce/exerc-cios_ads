package lista1;
import java.util.Scanner;
public class Produtalho
 {  /*Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre uns negócios lá */
    public static void main(String[] args) {
        Scanner calc = new Scanner(System.in);
            System.out.println("Digite |DOIS| números |InteIroS| e |UM| |RealR$|: "); 
                int n1 = calc.nextInt();
                int n2 = calc.nextInt();
                double n3 = calc.nextDouble();
                double res1 = n1 * (n2 / 2.0);
                double res2 = (3* n1) + n3 ;
                double res3 = Math.pow (n3,3);
            System.out.printf("Resultados:\nProduto do primeiro com a metade do segundo: %f\nSoma do tripo do primeiro com o terceiro: %f\nTerceiro número ao cubo: %f",res1,res2,res3);
        calc.close();
    }
}