package lista1;
import java.util.Scanner;
public class SeuJao {
    public static void main(String[] args) {
        /* Seu João precisa fazer um empréstimo automático no aplicativo. 
           O banco aprova a transação de acordo com as seguintes condições:
           Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
           Se a prestação for maior que 20% do salário, imprima: 
           "Empréstimo não concedido", caso contrário imprima: "Empréstimo concedido". */

        Scanner roubo = new Scanner(System.in);

        System.out.println("Informe o seu salário: \nE informe o valor da prestação do empréstimo:");
        double salario = roubo.nextDouble();
        double prestacao = roubo.nextDouble();

        if (prestacao > 0.2 * salario) {
            System.out.printf("Empréstimo de R$ %.2f não concedido. A prestação excede 20%% do salário de R$ %.2f.%n", prestacao, salario);
        } else {
            System.out.printf("Empréstimo de R$ %.2f concedido com sucesso!%n", prestacao);
        }

        roubo.close();
    }
}