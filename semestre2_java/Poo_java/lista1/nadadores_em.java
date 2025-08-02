package lista1;
import java.util.Scanner;
public class nadadores_em {
    /*
    Classificação por idade:
    - Infantil: 5 a 12 anos
    - Juvenil: 13 a 17 anos
    - Sênior: 18 anos ou mais
    */
    public static void main(String[] args) {
        Scanner idade_nadador = new Scanner(System.in);
        System.out.print("Informe a idade do nadador: ");
            int idade = idade_nadador.nextInt();
            if (idade >= 5 && idade <= 12) {
                System.out.printf("Categoria: Infantil (idade %d)%n", idade);
            } else if (idade >= 13 && idade <= 17) {
                System.out.printf("Categoria: Juvenil (idade %d)%n", idade);
            } else if (idade >= 18) {
                System.out.printf("Categoria: Sênior (idade %d)%n", idade);
            } else {
                System.out.println("Idade abaixo da faixa mínima para nadadores.");
            }
        idade_nadador.close();
    }
}
