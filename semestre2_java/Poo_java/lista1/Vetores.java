package lista1;
import java.util.Scanner;
public class Vetores {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
            int numero = 5;
            int vetor[] = new int[numero];
            int item;
        for (item = 0; item < numero; item ++){
            System.out.printf("Informe %2dºo. Valor de %d ", (item + 1),numero);
            vetor[item] = entrada.nextInt();
            }
        entrada.close();
    }
}
/*     ===================Segunda versão funcional====================
        Scanner vetior = new Scanner(System.in);

        System.out.print("Manda umas frutas aí (separadas por espaço): ");
        String entrada = vetior.nextLine(); 

        String[] frutas = entrada.split(" "); 

        if (frutas.length > 1) {
            String fruta_preferida = frutas[1]; 
            System.out.printf("Minha fruta preferida é %s\n", fruta_preferida);
        } else {
            System.out.println("Você precisa digitar pelo menos duas frutas!");
        }

        System.out.println("Todas as frutas digitadas:");
        for (int item = 0; item < frutas.length; item++) {
            System.out.println(frutas[item]);
        }

        vetior.close();
    }
}
 ===================Primeira versão não funcional=================
    public static void main(String[] args) {
        Scanner vetior = new Scanner(System.in);
        System.out.print("Manda umas frutas ai: ");
            String[] frutas = vetior.next();
            String fruta_preferida = frutas[1];
            System.out.printf("Minha fruta preferida é %s",fruta_preferida);
        for (int item = 0; item < frutas.length; item++){
            System.out.println(frutas[1]);
        }
*/
   
/*
         
         
         ==============VETOR 2===================
         System.out.print("Digite um número: ");
            int tamanho = vetior.nextInt();
            int[] vetor = new int[tamanho];   
            vetior.close();
            
                
            for (int item = 0; item < tamanho; item++){
                System.out.printf("Vetor na posição %d é %d\n",item,vetor[item]);

            }




       ===========VETOR 1==========
        int[] vetor = new int[10];
        vetor[0] = 10;
        vetor[1] = vetor[0] + 10;
        System.out.println(vetor[1]);
*/
