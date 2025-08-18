package lista2;
import java.util.Scanner;
public class ginastica_MonkaS_em {
    /*Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior
nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um
programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em
sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar
o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Thiago Almeida
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Thiago Almeida
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04  */
    public static void main(String[] args) {
        Scanner Giotto = new Scanner(System.in);

        System.out.print("Nome do atleta: ");
        String nome = Giotto.nextLine();

        double[] notas = new double[7];
        double soma = 0, maior = Double.MIN_VALUE, menor = Double.MAX_VALUE;

        for (int item = 0; item < 7; item++) {
            System.out.print("Nota " + (item+1) + ": ");
            notas[item] = Giotto.nextDouble();
            soma += notas[item];
            if (notas[item] > maior) maior = notas[item];
            if (notas[item] < menor) menor = notas[item];
        }

        double media = (soma - maior - menor) / 5;

        System.out.println("\nResultado final:");
        System.out.println("Atleta: " + nome);
        System.out.println("Melhor nota: " + maior);
        System.out.println("Pior nota: " + menor);
        System.out.println("Média: " + media);
        Giotto.close();
    }
}