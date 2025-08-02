package lista1;
import java.util.Scanner;
public class Vou_sonegar_imposto_de_renda_em {
/*40. Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, Crie um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
IR (11%) INSS (8%) Sindicato (5 %) */
    public static void main(String[] args) {
        Scanner impostometro = new Scanner(System.in);
            System.out.print("Quanto você ganha por hora? R$ ");
            double valor_hora = impostometro.nextDouble();
            System.out.print("Quantas horas você trabalhou no mês? ");
            int hora_mes = impostometro.nextInt();
            double salario_bruto = valor_hora * hora_mes;
            double desconto_ir = salario_bruto * 0.11;
            double desconto_inss = salario_bruto * 0.08;
            double desconto_sindicato = salario_bruto * 0.05;
            double salarioLiquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato;
            System.out.printf("Salário Bruto: R$ %.2f%n", salario_bruto);
            System.out.printf("Desconto IR (11%%): R$ %.2f%n", desconto_ir);
            System.out.printf("Desconto INSS (8%%): R$ %.2f%n", desconto_inss);
            System.out.printf("Desconto Sindicato (5%%): R$ %.2f%n", desconto_sindicato);
            System.out.printf("Salário Líquido: R$ %.2f%n", salarioLiquido);
        impostometro.close();
    }
}
