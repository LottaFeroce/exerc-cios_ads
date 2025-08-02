package lista1;
import java.util.Scanner;
public class lanchonete_em {
    /*
    Programa que calcula o valor de um pedido baseado no código e quantidade informados.
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
