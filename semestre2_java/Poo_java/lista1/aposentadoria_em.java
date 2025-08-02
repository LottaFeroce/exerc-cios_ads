package lista1;
import java.util.Scanner;
public class aposentadoria_em {
/*
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
*/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a idade do trabalhador: ");
        int idade = scanner.nextInt();
        System.out.print("Digite o tempo de serviço (em anos) do trabalhador: ");
        int tempoDeServico = scanner.nextInt();
        if (idade >= 65) {
            System.out.println("O trabalhador pode se aposentar (idade >= 65 anos).");
        } else if (tempoDeServico >= 30) {
            System.out.println("O trabalhador pode se aposentar (tempo de serviço >= 30 anos).");
        } else if (idade >= 60 && tempoDeServico >= 25) {
            System.out.println("O trabalhador pode se aposentar (idade >= 60 anos e tempo de serviço >= 25 anos).");
        } else {
            System.out.println("O trabalhador NÃO pode se aposentar.");
        }
        scanner.close();
    }
}
