import java.util.Scanner;
public class faxaria {
    public static void main(String[] args) {
        Scanner text = new Scanner(System.in);
        System.out.println("Digite Sim/Não");
        var confirm = text.next();
        System.out.println("Texto digitado: "+confirm);
        text.close();
    }

}
/*
    public static void main(String[] args) {
        int idade = 0;
        Scanner velhice = new Scanner(System.in);
        System.out.println("Digite sua idade: ");
        idade = velhice.nextInt();
        if(idade <=12){
            System.out.println("Abominação da Natureza");
        }else if(idade >12 && idade <=17){
            System.out.println("Adolorador profissional");
        }else if(idade >17 && idade <=59){
            System.out.println("Adfeast inprudentus");
        }else{
            System.out.println("Sybau💔🥀");
        }
        velhice.close();

}
}
 */