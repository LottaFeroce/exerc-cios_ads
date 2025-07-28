package lista1;
import java.util.Scanner;
public class troca_n {
    public static void main(String[] args) {
        Scanner trocadero = new Scanner(System.in);
        System.out.println("Digite varios números, no maximo 2: ");
        int a = trocadero.nextInt();
        int b = trocadero.nextInt();
        int temporaria = a;
        a = b;
        b = temporaria;
        System.out.println("Os números foram invertidos: "+a+" "+b);
        trocadero.close();

    }
    
}
