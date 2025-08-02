package lista1;
import java.util.Scanner;
public class IMC_deVerdadeagr_em {
/*Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a
tabela abaixo:
IMC Classificação
< 18,5 Abaixo do Peso
18,6 - 24,9 Saudável
25,0 - 29,9 Peso em excesso
30,0 - 34,9 Obesidade Grau I
35,0 - 39,9 Obesidade Grau II (severa)
≥ 40,0 Obesidade Grau III (mórbida) */
    public static void main(String[] args) {
        Scanner peso_imc = new Scanner(System.in);
        System.out.print("Digite o peso (em kg): ");
            double peso = peso_imc.nextDouble();
            System.out.print("Digite a altura (em metros): ");
            double altura = peso_imc.nextDouble();
            double imc = peso / (altura * altura);
            System.out.printf("Seu IMC é: %.2f%n", imc);
            if (imc < 18.5) {
                    System.out.println("Classificação: Abaixo do Peso");
                } else if (imc <= 24.9) {
                    System.out.println("Classificação: Saudável");
                } else if (imc <= 29.9) {
                    System.out.println("Classificação: Peso em excesso");
                } else if (imc <= 34.9) {
                    System.out.println("Classificação: Obesidade Grau I");
                } else if (imc <= 39.9) {
                    System.out.println("Classificação: Obesidade Grau II (severa)");
            }else {
                System.out.println("Classificação: Obesidade Grau III (mórbida)");
            }
        peso_imc.close();
    }
}
