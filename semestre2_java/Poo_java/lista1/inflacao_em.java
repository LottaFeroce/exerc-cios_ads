package lista1;
import java.util.Scanner;
public class inflacao_em {
    /*
    Calcula o novo preço de um produto com base na faixa de inflação:
    - Até R$ 50: aumento de 5%
    - De R$ 50,01 até R$ 100: aumento de 10%
    - Acima de R$ 100: aumento de 15%
    */
    public static void main(String[] args) {
        Scanner produto_tarifado = new Scanner(System.in);
        System.out.print("Informe o valor antigo do produto: R$ ");
            double valor_antigo = produto_tarifado.nextDouble();
            double valor_atual = 0.0;
            double percentual = 0.0;
            if (valor_antigo <= 50) {
                percentual = 0.05;
            } else if (valor_antigo <= 100) {
                percentual = 0.10;
            } else {
                percentual = 0.15;
            }
            valor_atual = valor_antigo + (valor_antigo * percentual);

        System.out.printf("\nValor antigo: R$ %.2f%n", valor_antigo);
        System.out.printf("\nPercentual de aumento: %.0f%%%n", percentual * 100);
        System.out.printf("\nNovo valor com reajuste: R$ %.2f%n", valor_atual);
        produto_tarifado.close();
    }
}
