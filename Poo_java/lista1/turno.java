package lista1;
import java.util.Scanner;
public class turno { /*Crie um programa que receba M para matutino, V para vespertino e N para noturno, após isso printe bom dia/boa tarde/boa noite */
    public static void main(String[] args) {
        Scanner turnoestudo = new Scanner(System.in);
        System.out.println("Informe qual turnoz |M| Matar o tino, |V| vespero, |N| Nontro:");
        String turno = turnoestudo.next();
            if (turno.equalsIgnoreCase("m")){
                System.out.println("Você est Mata utino!!!!!!!!");
            }else if (turno.equalsIgnoreCase("v")){
                System.out.println("Estudas en el Vespertine");
            }else if (turno.equalsIgnoreCase("N")){
                System.out.println("Not urno ojojoj");
            }else{
                System.out.println("Vazou o seu ip. ->127.0.0.0<-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
            }
        turnoestudo.close();
    }
    
}
