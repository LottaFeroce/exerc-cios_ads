package lista1;
import java.util.Scanner;
public class Calculadora_v2_comWhile_em {
    public static void main(String[] args) {
        Scanner calculad = new Scanner(System.in);
        int operador;  
        do {
            System.out.println("\nQual operação deseja realizar?\n|1| Para Adição\n|2| Para Subtração\n|3| Para Multiplicação\n|4| Para Divisão\n|5| Para Finalizar");
            operador = calculad.nextInt(); 
            if (operador >= 1 && operador <= 4) {            
                System.out.print("Digite o primeiro valor: ");
                double num1 = calculad.nextDouble();
                System.out.print("Digite o segundo valor: ");
                double num2 = calculad.nextDouble();
                double resultado = 0;        
                switch (operador) {
                    case 1:
                        resultado = num1 + num2;
                        System.out.printf("\nResultado da soma: %.2f%n", resultado);
                        break;
                    case 2:
                        resultado = num1 - num2;
                        System.out.printf("\nResultado da subtração: %.2f%n", resultado);
                        break;
                    case 3:
                        resultado = num1 * num2;
                        System.out.printf("\nResultado da multiplicação: %.2f%n", resultado);
                        break;
                    case 4:
                        if (num2 != 0) {
                            resultado = num1 / num2;
                            System.out.printf("\nResultado da divisão: %.2f%n", resultado);
                        }else{
                            System.out.println("\nErro: divisão por zero não é permitida!");
                        }
                        break;
                }
            } else if (operador == 5) {
                System.out.println("\nSistema finalizado. Até mais");
            } else {
                System.out.println("\nValor inválido! Escolha uma opção entre 1 e 5.");
            }
        } while (operador != 5);  
        calculad.close();
    }
}
