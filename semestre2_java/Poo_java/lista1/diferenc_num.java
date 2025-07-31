
import java.util.Scanner;
public class diferenc_num {/*Crie um programa que receba 2 números mostre o maior[informe a diferenca entre eles e se forem iguais exc 12 & 13] */
    public static void main(String[] args) {
        Scanner difef = new Scanner(System.in);
            System.out.println("Informe dois números: ");
                int n1 = difef.nextInt();
                int n2 = difef.nextInt();
                double diferencial;
                diferencial = n1 - n2;
            if(n1 > n2){
                System.out.printf("O primeiro número %d é maior que o segundo %d com diferencial de %.2f ente um e o outro",n1,n2,diferencial);
            }else if(n2>n1){
                System.out.printf("O segundo número %d é maior que o primeiro %d com diferencial de %.2f entre um e o outro",n2,n1,diferencial);
            }else if (n1==n2){
                System.out.println("Valores iguais");
            }else{
                System.out.println("Valor inevitavel");
            }
        difef.close();
    }
}
