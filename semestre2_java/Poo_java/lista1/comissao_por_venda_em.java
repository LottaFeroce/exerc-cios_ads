package lista1;
import java.util.Scanner;
public class comissao_por_venda_em {
/*Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
vendedor. Para calcular a comissão, considere a tabela abaixo:
Venda mensal Comissão
Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
Menor que R$20.000,00 R$400,00 +14% das vendas
*/
      public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Informe o valor da venda: R$ ");
            double valor_venda = input.nextDouble();
            double comissao = 0.0;
            if (valor_venda >= 100000) {
                comissao = 700 + (0.16 * valor_venda);
            } else if (valor_venda >= 80000) {
                comissao = 650 + (0.14 * valor_venda);
            } else if (valor_venda >= 60000) {
                comissao = 600 + (0.14 * valor_venda);
            } else if (valor_venda >= 40000) {
                comissao = 550 + (0.14 * valor_venda);
            } else if (valor_venda >= 20000) {
                comissao = 500 + (0.14 * valor_venda);
            } else {
                comissao = 400 + (0.14 * valor_venda);
            }
        System.out.printf("Valor da venda: R$ %.2f%n", valor_venda);
        System.out.printf("Comissão a ser paga: R$ %.2f%n", comissao);
        input.close();
    }
}
