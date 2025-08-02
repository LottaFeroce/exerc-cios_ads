package lista1;
import java.util.Scanner;
public class Delta_segundo_grau_em {
/*Calcule as raízes da equação de 2o grau.
Lembrando que:
Onde
∆ = B2−4ac
E ax2+ bx + c = 0 representa uma equação de 2o grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação
de segundo grau”.
i. Se ∆ < 0, não existe real. Imprima a mensagem: Não existe raiz.
ii. Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única.
iii. Se ∆ ≥ 0, imprima as duas raízes reais.*/
    public static void main(String[] args) {
        Scanner delta_equacionado = new Scanner(System.in);
            System.out.print("Digite o valor de a: ");
            double a = delta_equacionado.nextDouble();
            System.out.print("Digite o valor de b: ");
            double b = delta_equacionado.nextDouble();
            System.out.print("Digite o valor de c: ");
            double c = delta_equacionado.nextDouble();
            if (a == 0) {
                System.out.println("Não é equação de segundo grau.");
            } else {
                double delta = b * b - 4 * a * c;
                if (delta < 0) {
                    System.out.println("Não existe raiz real.");
                } else if (delta == 0) {
                    double raiz_unica = -b / (2 * a);
                    System.out.printf("Raiz única: %.2f%n", raiz_unica);
                } else {
                    double raiz1 = (-b + Math.sqrt(delta)) / (2 * a);
                    double raiz2 = (-b - Math.sqrt(delta)) / (2 * a);
                    System.out.printf("Duas raízes reais:\nRaiz 1: %.2f\nRaiz 2: %.2f%n", raiz1, raiz2);
                }
        }
        delta_equacionado.close();
    }
}

