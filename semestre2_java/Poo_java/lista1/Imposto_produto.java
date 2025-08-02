package lista1;
import java.util.Scanner;
public class Imposto_produto {
/* Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
não for válido, mostrar uma mensagem de erro.
 */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor do produto: R$\nE digite o estado de destino (MG, SP, RJ, MS):  ");
        double valorProduto = scanner.nextDouble();
        String estado = scanner.next().toUpperCase(); 
        double imposto = 0.0;
        double precoFinal = 0.0;
        switch (estado) {
            case "MG":
                imposto = 0.07; 
                break;
            case "SP":
                imposto = 0.12; 
                break;
            case "RJ":
                imposto = 0.15; 
                break;
            case "MS":
                imposto = 0.08; 
                break;
            default:
                System.out.println("Erro: Estado inválido.");
                scanner.close();
                return; 
        }
        precoFinal = valorProduto + (valorProduto * imposto);
        System.out.printf("O preço final do produto, com imposto de %.0f%%, é: R$ %.2f%n", imposto * 100, precoFinal);
        scanner.close();
    }
}
