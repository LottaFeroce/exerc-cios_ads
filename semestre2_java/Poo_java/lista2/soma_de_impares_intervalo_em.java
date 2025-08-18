package lista2;
import java.util.Scanner;
public class soma_de_impares_intervalo_em {
    /*Faça um programa que some os números ímpares contidos em um intervalo definido pelo
usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa
deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um
intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma
mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de
tela de saída:
Digite o valor inicial e valor final: 5
10
Soma dos ímpares neste intervalo: 21  */
    public static void main(String[] args) {
        Scanner Rhinoceros_beetle = new Scanner(System.in);
        System.out.print("Digite o valor inicial: ");
        int inicio = Rhinoceros_beetle.nextInt();
        System.out.print("Digite o valor final: ");
        int fim = Rhinoceros_beetle.nextInt();

        if (inicio > fim) {
            System.out.println("Intervalo de valores invalido");
        } else {
            int soma = 0;
            for (int item = inicio; item <= fim; item++) {
                if (item % 2 != 0) soma += item;
            }
            System.out.println("Soma dos ímpares neste intervalo: " + soma);
        }
        Rhinoceros_beetle.close();
    }
}