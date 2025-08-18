package lista2;
import java.util.Scanner;
public class calculo_de_potenciacao_em {
    /*Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3
x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente (y)
e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para resolver o
problema utilize estrutura de repetição. 
 */
  public static void main(String[] args) {
        Scanner calc_potencia = new Scanner(System.in);
        System.out.print("Digite a base (x): ");
        int base = calc_potencia.nextInt();
        System.out.print("Digite o expoente (y): ");
        int expoente = calc_potencia.nextInt();

        int resultado = 1;
        for (int item = 0; item < expoente; item++) {
            resultado *= base;
        }

        System.out.println(base + "^" + expoente + " = " + resultado);
        calc_potencia.close();
    }
}