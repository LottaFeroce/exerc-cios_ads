package lista1;
import java.util.Scanner;
public class media_ponderada {
    /*
    Crie um algoritmo que calcule a média ponderada das notas de 3 provas.
    A primeira e a segunda prova têm peso 1 e a terceira tem peso 2.
    Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
    A nota para aprovação deve ser igual ou superior a 60 pontos.
    */
    public static void main(String[] args) {
        Scanner mediaP = new Scanner(System.in);
        System.out.print("Diga quais foram as suas três notas: ");
        double nota1 = mediaP.nextDouble();
        double nota2 = mediaP.nextDouble();
        double nota3 = mediaP.nextDouble();
        if ((nota1 >= 0 && nota1 <= 10) && 
           (nota2 >= 0 && nota2 <= 10) &&
           (nota3 >= 0 && nota3 <= 10)) {
            int pesoTotal = 4;
            double notapeso1 = nota1 * 1;
            double notapeso2 = nota2 * 1;
            double notapeso3 = nota3 * 2;
            double soma_pontos = notapeso1 + notapeso2 + notapeso3;
            double media = soma_pontos / pesoTotal;
            System.out.printf("A média do aluno é: %.2f%n", media);
            if (media * 10 >= 60) { 
                System.out.println("Aluno aprovado!");
            } else {
                System.out.println("Aluno reprovado.");
            }
        } else {
            System.out.println("Uma ou mais notas são inválidas. Encerrando o programa.");
        }
        mediaP.close();
    }
}