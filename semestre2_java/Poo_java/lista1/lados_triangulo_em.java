package lista1;
import java.util.Scanner;
public class lados_triangulo_em {
/*Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
• Chama-se equilátero o triângulo que tem três lados iguais.
• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
*/
    public static void main(String[] args) {
        Scanner ladangulo = new Scanner(System.in);
        System.out.println("Para determinar o tipo do triângulo, informe os valores de seus lados |A|B|C|: ");
        double lado_A = ladangulo.nextDouble();
        double lado_B = ladangulo.nextDouble();
        double lado_C = ladangulo.nextDouble();
        if ((lado_A < lado_B + lado_C) && (lado_B < lado_A + lado_C) && (lado_C < lado_A + lado_B)) {
            if (lado_A == lado_B && lado_B == lado_C) {
                System.out.println("Triângulo Equilátero");
            } else if (lado_A == lado_B || lado_B == lado_C || lado_A == lado_C) {
                System.out.println("Triângulo Isósceles");
            } else {
                System.out.println("Triângulo Escaleno");
            }
        } else {
            System.out.println("Os valores informados não formam um triângulo.");
        }
        ladangulo.close();
    }
}
