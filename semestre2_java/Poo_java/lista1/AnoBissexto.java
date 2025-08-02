package lista1;
import java.util.Scanner;
public class AnoBissexto {
    /*
    Determine se um determinado ano lido é bissexto.
    Um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
    Exemplo de anos bissextos: 1988, 1992, 1996.
    */
    public static void main(String[] args) {
        Scanner anobis = new Scanner(System.in);
        System.out.print("Informe o ano para validação: ");
        int ano_atual = anobis.nextInt();
        if ((ano_atual % 4 == 0 && ano_atual % 100 != 0) || (ano_atual % 400 == 0)) {
            System.out.println("Ano é bissexto");
        } else {
            System.out.println("Ano não é bissexto");
        }
        anobis.close();
    }
}
