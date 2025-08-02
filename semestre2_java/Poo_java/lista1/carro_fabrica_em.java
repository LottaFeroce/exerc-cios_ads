package lista1;
import java.util.Scanner;
public class carro_fabrica_em {
/*O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do
distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
CUSTO DE FÁBRICA % DO DISTRIBUIDOR % DOS IMPOSTOS
até R$12.000,00 5 isento
entre R$12.000,00 e 25.000,00 10 15
acima de R$25.000,00 15 20 */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            System.out.print("Informe o custo de fábrica do carro: R$ ");
            double custoFabrica = scanner.nextDouble();
            double percentualDistribuidor = 0;
            double percentualImpostos = 0;
            if (custoFabrica <= 12000) {
                    percentualDistribuidor = 0.05;
                    percentualImpostos = 0.0;
                } else if (custoFabrica <= 25000) {
                    percentualDistribuidor = 0.10;
                    percentualImpostos = 0.15;
            }else {
                percentualDistribuidor = 0.15;
                percentualImpostos = 0.20;
            }
            double valorDistribuidor = custoFabrica * percentualDistribuidor;
            double valorImpostos = custoFabrica * percentualImpostos;
            double custoConsumidor = custoFabrica + valorDistribuidor + valorImpostos;
            System.out.printf("O custo ao consumidor será: R$ %.2f%n", custoConsumidor);
        scanner.close();
    }
}
