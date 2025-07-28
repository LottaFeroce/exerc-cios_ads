package lista1;
import java.util.Scanner;
public class Salario_Funcionario {
    public static void main(String[] args) {
        Scanner roubo = new Scanner(System.in);
        double VALOR_HORA = 40.50;
        double LIMITE_IR = 2500.00;
        double ALIQUOTA_IR = 0.11;
        System.out.print("Informe o número de horas trabalhadas: ");
        double horasTrabalhadas = roubo.nextDouble();
        double salarioBruto = horasTrabalhadas * VALOR_HORA;
        double imposto = 0.0;
        if (salarioBruto > LIMITE_IR) {
            imposto = salarioBruto * ALIQUOTA_IR;
        }
        double salarioLiquido = salarioBruto - imposto;
        System.out.printf(" Salário bruto: R$ %.2f%n Imposto de renda: R$ %.2f%n Salário líquido: R$ %.2f%n",
        salarioBruto,imposto,salarioLiquido);
        roubo.close();
    }
}
