package lista1;
import java.util.Scanner;
public class par_impar {
    public static void main(String[] args) {
        Scanner parimpar = new Scanner(System.in);
        System.out.println("Digite algum número ae tlg: ");
        int numero = parimpar.nextInt();
        if (numero % 2 == 0){
            System.out.println("O número é PAr");
        }else{
            System.out.println("O número é impar");
        }
        
        parimpar.close();
    }
    
}
