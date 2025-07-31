package lista1;
import java.util.Scanner;
public class M10 {/*Cire um ahhhhhhhhhhh maior qye qi i 10!!! */
    public static void main(String[] args) {
        Scanner maior = new Scanner(System.in);
        System.out.println("Digite um número possivelmente maior que 10: ");
        int numero = maior.nextInt();
        if(numero < 0){
            System.out.println("números positivos, abominação");
        }else if(numero <10){
            System.out.println("men10");
        }else{
            System.out.println("Adfeast inprudentus");
        

        maior.close();
    }
}
}
