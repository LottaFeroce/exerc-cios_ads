package lista1;
import java.util.Scanner;
public class mai_men {/*Crie um programa que receba dois números e informe qual é o maior */
    public static void main(String[] args) {
        Scanner maimen = new Scanner(System.in);
        System.out.println("Informe dois números inteiros e veja qual é maior:");
        int n1 = maimen.nextInt();
        int n2 = maimen.nextInt();
        if (n1>n2){
            System.out.printf("O primeiro número: %d é maior que o segundo número: %d",n1,n2);
        }else{
            System.out.printf("O segundo número: %d é maior que o primeiro número: %d",n2,n1);
        }


        maimen.close();
    }
    
}
