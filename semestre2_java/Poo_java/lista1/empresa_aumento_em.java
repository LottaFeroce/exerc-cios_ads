package lista1;
import java.util.Scanner;
public class empresa_aumento_em {
/*
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que
considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
salário terão um aumento proporcionalmente maior do que os funcionários com um salário
maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
adicional de salário. Crie um programa que leia:
• o valor do salário atual do funcionário;
• o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum
aumento.
Salário Atual Reajuste (%) Tempo de Serviço Bônus
Até 500,00 25% Abaixo de 1 ano Sem bônus
Até 1000,00 20% De 1 a 3 anos 100,00
Até 1500,00 15% De 4 a 6 anos 200,00
Até 2000,00 10% De 7 a 10 anos 300,00
Acima de 2000,00 Sem reajuste Mais de 10 anos 500,00
*/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Informe o salário atual do funcionário: ");
        double salario = scanner.nextDouble();
        System.out.print("Informe o tempo de serviço (em anos): ");
            int tempoServico = scanner.nextInt();
            double reajuste = 0;
            double bonus = 0;
            if (salario <= 500) {
                    reajuste = salario * 0.25;
                } else if (salario <= 1000) {
                    reajuste = salario * 0.20;
                } else if (salario <= 1500) {
                    reajuste = salario * 0.15;
                } else if (salario <= 2000) {
                    reajuste = salario * 0.10;
                }
                if (tempoServico >= 1 && tempoServico <= 3) {
                    bonus = 100;
                } else if (tempoServico >= 4 && tempoServico <= 6) {
                    bonus = 200;
                } else if (tempoServico >= 7 && tempoServico <= 10) {
                    bonus = 300;
                } else if (tempoServico > 10) {
                    bonus = 500;
                }
            if (reajuste == 0 && bonus == 0) {
                    System.out.println("O funcionário não tem direito a aumento.");
            }else {
                double novoSalario = salario + reajuste + bonus;
                System.out.printf("O novo salário do funcionário é: R$ %.2f%n", novoSalario);
            }
        scanner.close();
    }
}
