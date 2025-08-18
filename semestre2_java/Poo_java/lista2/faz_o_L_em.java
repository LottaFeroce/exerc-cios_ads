package lista2;
import java.util.Scanner;
public class faz_o_L_em {
    /*Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de
código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2-
João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
▪ O total de votos para cada candidato;
▪ O total de votos nulos;
▪ O total de votos em branco;
▪ A percentagem de votos nulos sobre o total de votos;
▪ A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto
de votos tem-se o valor zero.  */
     public static void main(String[] args) {
        Scanner Secret_Emperor = new Scanner(System.in);

        int[] candidatos = new int[4];
        int nulos = 0, brancos = 0, voto;

        System.out.println("Códigos: 1-José, 2-João, 3-Maria, 4-Ana, 5-Nulo, 6-Branco");

        while (true) {
            System.out.print("Digite seu voto (0 para encerrar): ");
            voto = Secret_Emperor.nextInt();
            if (voto == 0) break;

            switch (voto) {
                case 1: case 2: case 3: case 4:
                    candidatos[voto - 1]++;
                    break;
                case 5: nulos++; break;
                case 6: brancos++; break;
                default: System.out.println("Voto inválido!");
            }
        }

        int total = candidatos[0] + candidatos[1] + candidatos[2] + candidatos[3] + nulos + brancos;

        System.out.println("\nResultado da eleição:");
        System.out.println("José: " + candidatos[0]);
        System.out.println("João: " + candidatos[1]);
        System.out.println("Maria: " + candidatos[2]);
        System.out.println("Ana: " + candidatos[3]);
        System.out.println("Nulos: " + nulos);
        System.out.println("Brancos: " + brancos);

        if (total > 0) {
            System.out.printf("%.2f Percentual de nulos: %.2f%%\n", (nulos * 100.0 / total), (nulos * 100.0 / total));
            System.out.printf("%.2f Percentual de brancos: %.2f%%\n", (brancos * 100.0 / total), (brancos * 100.0 / total));
        }
        Secret_Emperor.close();
    }
}