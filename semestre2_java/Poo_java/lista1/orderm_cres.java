package lista1;
import java.util.Scanner;
public class orderm_cres {/*Crie um programa que receba três números e informe se os mesmos estão em ordem crescente */
    public static void main(String[] args) {
        Scanner ordem = new Scanner(System.in);
        System.out.println("Informe três números oiefhpppuçi ordem cr´ksadnsente: ");
        int n1 = ordem.nextInt();
        int n2 = ordem.nextInt();
        int n3 = ordem.nextInt();
        if (n1 <= n2 && n2 <= n3){
            System.out.printf("Os números estão em ordem crescente: %d, %d, %d",n1,n2,n3);
        }else{
            System.out.printf("Os números não estão em ordem crescente");
        }
        ordem.close();
    }
    
}
