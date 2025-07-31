package lista1;
import java.util.Scanner;
public class Imc_java_em {
    public static void main(String[] args) {
        /*Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
        utilizando as seguintes formulas (onde h corresponde à altura):
        • Homens: (72.7∗ h)−58
        • Mulheres: (62,1∗ h)−44,7 */
        Scanner imc = new Scanner(System.in);
            System.out.println("Informe o seu gênero e sua altura: ");
            String gen = imc.nextLine();
            double altura = imc.nextDouble();
            if (gen.equalsIgnoreCase("f")) {
                double calc_imc = (altura * 62.1)-44.7;
                System.out.printf("Sexo feminino e o seu IMC é: %.2f",calc_imc);
            } else if (gen.equalsIgnoreCase("m")) {
                double calc_imc = (altura * 72.7)-58;
                System.out.printf("Sexo masculino e o seu IMC é: %.2f",calc_imc);
                }else{
            System.out.println("Informe um gênero que exista ou vá a um psicólogo!!!!!   ");
            }
        imc.close();

    } 
}
