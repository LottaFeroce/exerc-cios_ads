package lista2;
import java.util.Scanner;
public class contagem_regr_while_em {
    /* Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
       iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após contagem. */
    public static void main(String[] args) {
        Scanner contagem = new Scanner(System.in);
        System.out.print("Informe um valor começando pelo menos em 10: ");
        int cont = contagem.nextInt();
        while (cont < 10) {
                System.out.println("Valor inválido! Informe um valor maior ou igual a 10: ");
                cont = contagem.nextInt();
            }
            while (cont >= 0) {
                System.out.println(cont);
                cont--;
        }
        System.out.println("FIM!");
        contagem.close();
    }
}
