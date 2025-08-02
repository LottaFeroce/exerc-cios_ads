package lista1;
import java.util.Scanner;
public class lanchonete_em {
    /*
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
abaixo:
Especificação Código Preço
Hot Dog 100 12.00
X-Salada 102 18.50
X-BACON 103 25.50
X-Burguer 104 17.00
Suco de Laranja 105 9.50
Refrigerante 106 6.00
    */
    public static void main(String[] args) {
        Scanner lanch_net = new Scanner(System.in);
        System.out.println("Bem-vindo à Lanchonete");
        System.out.println("Menu:");
        System.out.println("|100| Hot Dog            - R$ 12.00");
        System.out.println("|102| X-Salada           - R$ 18.50");
        System.out.println("|103| X-BACON            - R$ 25.50");
        System.out.println("|104| X-Burguer          - R$ 17.00");
        System.out.println("|105| Suco de Laranja    - R$ 9.50");
        System.out.println("|106| Refrigerante       - R$ 6.00");
        System.out.print("\nDigite o código do produto desejado: ");
        int cod = lanch_net.nextInt();
        System.out.print("Digite a quantidade desejada: ");
        int qtd = lanch_net.nextInt();
        double valorTotal = 0;
        String produto = "";
        switch (cod) {
            case 100:
                valorTotal = 12.00 * qtd;
                produto = "Hot Dog";
                break;
            case 102:
                valorTotal = 18.50 * qtd;
                produto = "X-Salada";
                break;
            case 103:
                valorTotal = 25.50 * qtd;
                produto = "X-BACON";
                break;
            case 104:
                valorTotal = 17.00 * qtd;
                produto = "X-Burguer";
                break;
            case 105:
                valorTotal = 9.50 * qtd;
                produto = "Suco de Laranja";
                break;
            case 106:
                valorTotal = 6.00 * qtd;
                produto = "Refrigerante";
                break;
            default:
                System.out.println("Código inválido!");
                lanch_net.close();
                return;
        }
        System.out.printf("\nVocê pediu %d x %s.%nTotal a pagar: R$ %.2f%n", qtd, produto, valorTotal);
        System.out.println("Obrigada pela preferência");
        lanch_net.close();
    }
}
