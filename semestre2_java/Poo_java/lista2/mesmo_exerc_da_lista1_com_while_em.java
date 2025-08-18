package lista2;
import java.util.Scanner;
public class mesmo_exerc_da_lista1_com_while_em {
    /*Crie um programa que apresente um menu de opções para o cálculo das seguintes operações
entre dois números.
• adição (opção 1)
• subtração (opção 2) • multiplicação (opção 3)
• divisão (opção 4).
• saída (opção 5)
• programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do
resultado e a volta ao menu de opções. O programa só termina quando for escolhida a
opção de saída (opção 5).  */
    public static void main(String[] args) {
        Scanner Via_Dolorosa = new Scanner(System.in);
        int opcao;

        do {
            System.out.print("\nMenu de Operações:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\nEscolha uma opção: ");
            opcao = Via_Dolorosa.nextInt();

            if (opcao >= 1 && opcao <= 4) {
                System.out.print("Digite o primeiro número: ");
                double a = Via_Dolorosa.nextDouble();
                System.out.print("Digite o segundo número: ");
                double b = Via_Dolorosa.nextDouble();

                switch (opcao) {
                    case 1: System.out.println("Resultado: " + (a + b)); break;
                    case 2: System.out.println("Resultado: " + (a - b)); break;
                    case 3: System.out.println("Resultado: " + (a * b)); break;
                    case 4: 
                        if (b != 0) System.out.println("Resultado: " + (a / b));
                        else System.out.println("Erro: divisão por zero!");
                        break;
                }
            }
        } while (opcao != 5);

        Via_Dolorosa.close();
        System.out.println("Programa encerrado.");
    }
}