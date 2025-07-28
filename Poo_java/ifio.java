import java.util.Scanner;
public class ifio {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite a quantidade de Bogos Binted: ");
        int numero = input.nextInt();
        System.out.println("Bogos Binted: "+numero);

        if (numero >= 1){
            System.out.println("Your Bogos got binted");
        }else{
            System.out.println("Bint your Bogos immediately");
        }
        input.close();

    }



    
}
