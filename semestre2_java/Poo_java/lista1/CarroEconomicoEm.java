package lista1;
import java.util.Scanner;
public class CarroEconomicoEm {
/*
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
Consumo (Km/l) Mensagem
menor que 8 Venda o carro!
entre 8 e 14 Econômico!
maior que 14 Super econômico!*/
    public static void main(String[] args) {
        Scanner dist = new Scanner(System.in);       
        System.out.print("Digite a distância em Km e a quantidade de litros consumidos: ");
        double kilomet = dist.nextDouble();
        double litros = dist.nextDouble();       
        if (kilomet > 0 && litros > 0) {
            double consumo = kilomet / litros;          
            System.out.printf("Consumo do carro: %.2f Km/l%n", consumo);         
            if (consumo < 8) {
                System.out.println("Venda o carro!");
            } else if (consumo >= 8 && consumo <= 14) {
                System.out.println("Econômico!");
            } else {
                System.out.println("Super econômico!");
            }
        } else {
            System.out.println("Valores inválidos! A distância e a quantidade de litros devem ser positivas.");
        }
        
        dist.close();
    }
}
