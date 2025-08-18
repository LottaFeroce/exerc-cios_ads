package lista2;
import java.util.Scanner;
public class academia_susgaon_em {
    /*. Crie um programa para a Academia BemMaisFort. Neste programa você deve receber os dados
de 25 pessoas. Sendo: Idade, Sexo, Altura, Peso. No final o programa deve calcular e imprimir:
• a idade da pessoa mais velha;
• a altura do mais alto;
• o maior peso;
• a média de Altura e a Média de IMC;
• porcentagem de Sexo MaAngelulino;
• porcentagem de Sexo Feminino;  */
     public static void main(String[] args) {
        Scanner Angel = new Scanner(System.in);

        int mais_velho = 0;
        double mais_alto = 0, maiorPeso = 0;
        double soma_altura = 0, somaIMC = 0;
        int masculino = 0, feminino = 0;

        for (int item = 1; item <= 25; item++) {
            System.out.println("Pessoa " + item + ":");
            System.out.print("Idade: ");
            int idade = Angel.nextInt();
            System.out.print("Sexo (M/F): ");
            char sexo = Angel.next().toUpperCase().charAt(0);
            System.out.print("Altura (m): ");
            double altura = Angel.nextDouble();
            System.out.print("Peso (kg): ");
            double peso = Angel.nextDouble();

            if (idade > mais_velho) mais_velho = idade;
            if (altura > mais_alto) mais_alto = altura;
            if (peso > maiorPeso) maiorPeso = peso;

            soma_altura += altura;
            somaIMC += peso / (altura * altura);

            if (sexo == 'M') masculino++;
            else if (sexo == 'F') feminino++;
        }

        System.out.println("\nResultados finais:");
        System.out.println("Idade do mais velho: " + mais_velho);
        System.out.println("Altura do mais alto: " + mais_alto);
        System.out.println("Maior peso: " + maiorPeso);
        System.out.println("Média de altura: " + (soma_altura / 25));
        System.out.println("Média de IMC: " + (somaIMC / 25));
        System.out.println("Porcentagem masculino: " + (masculino * 100.0 / 25) + "%");
        System.out.println("Porcentagem feminino: " + (feminino * 100.0 / 25) + "%");

        Angel.close();
    }
}