package lista2;
import java.util.Scanner;
public class aumento_salario_em {
    /*Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020 recebeu
aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do ano
anterior. Faça um programa que determine o salário atual do funcionário.  */
    public static void main(String[] args) {
        System.out.print("Digite qual foi o seu salário: ");
        Scanner salazar = new Scanner(System.in);
        double salario = salazar.nextDouble();
        double aumento = 0.015; 

        salario += salario * aumento; 

        for (int ano = 2021; ano <= 2025; ano++) { 
            aumento *= 2;
            salario += salario * aumento;
        }

        System.out.printf("Salário atual: %.2f R$ " ,salario);
        salazar.close();
    }
}