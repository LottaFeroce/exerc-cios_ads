
package lista1;
import java.util.Scanner;
public class media_avaliacao {    
    /*
A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
aprovado. Crie todas as verificações necessárias
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite a nota do Trabalho de Laboratório:\nA nota da Avaliação Semestral:\nA nota do exame final: ");
        double notaLab = input.nextDouble();
        double notaSem = input.nextDouble();
        double notaExame = input.nextDouble();

        if ((notaLab >= 0 && notaLab <= 10) &&
            (notaSem >= 0 && notaSem <= 10) &&
            (notaExame >= 0 && notaExame <= 10)) {

            double media = (notaLab * 2 + notaSem * 3 + notaExame * 5) / 10;

            System.out.printf("A média ponderada do aluno é: %.2f%n", media);

            if (media >= 0 && media <= 2.9) {
                System.out.println("Resultado: Reprovado ");
            } else if (media >= 3.0 && media <= 5.9) {
                System.out.println("Resultado: Recuperação ");
            } else {
                System.out.println("Resultado: Aprovado ");
            }
        } else {
            System.out.println("Uma ou mais notas estão inválidas. As notas devem estar entre 0 e 10.");
        }
        input.close();
    }
}
