package lista1;
import java.util.Scanner;
public class calculadora_java_em {
    /*
    Crie uma mini calculadora que mostra ao usuário um menu com 4 opções de operações matemáticas.
    O usuário escolhe uma das opções, informa dois valores e o programa realiza a operação e mostra o resultado.
    */
    public static void main(String[] args) {
        Scanner calculad = new Scanner(System.in);
        System.out.println("Qual operação deseja realizar?");
        System.out.println("|1| Para Adição");
        System.out.println("|2| Para Subtração");
        System.out.println("|3| Para Multiplicação");
        System.out.println("|4| Para Divisão");
        System.out.println("|5| Para Finalizar");
        int operador = calculad.nextInt();
        if (operador >= 1 && operador <= 4) {
            System.out.print("Digite o primeiro valor: ");
            double num1 = calculad.nextDouble();
            System.out.print("Digite o segundo valor: ");
            double num2 = calculad.nextDouble();
            double resultado = 0;
            switch (operador) {
                case 1:
                    resultado = num1 + num2;
                    System.out.printf("Resultado da soma: %.2f%n", resultado);
                    break;
                case 2:
                    resultado = num1 - num2;
                    System.out.printf("Resultado da subtração: %.2f%n", resultado);
                    break;
                case 3:
                    resultado = num1 * num2;
                    System.out.printf("Resultado da multiplicação: %.2f%n", resultado);
                    break;
                case 4:
                    if (num2 != 0) {
                        resultado = num1 / num2;
                        System.out.printf("Resultado da divisão: %.2f%n", resultado);
                    } else {
                        System.out.println("Erro: divisão por zero não é permitida!");
                    }
                    break;
            }
        } else if (operador == 5) {
            System.out.println("Sistema finalizado. Até mais");
        } else {
            System.out.println("Valor inválido! Escolha uma opção entre 1 e 5.");
        }
        calculad.close();
    }
}