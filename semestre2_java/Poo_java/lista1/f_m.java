package lista1;
import java.util.Scanner;
public class f_m {/*crie um programa que indique o sexo baseado nas informações digitadas */
    public static void main(String[] args) {
        Scanner secs = new Scanner(System.in);
        System.out.println("Informe o seu Gênero com F ou M [Só existem DOIS]:");
        String gen = secs.next();
        if (gen.equalsIgnoreCase("f")) {
            System.out.println("Feminino");
        } else if (gen.equalsIgnoreCase("m")) {
            System.out.println("Masculino");
            }else{
        System.out.println("Informe um gênero que exista ou vá a um psicólogo!!!!!   ");
        }
    secs.close();
    }
}
