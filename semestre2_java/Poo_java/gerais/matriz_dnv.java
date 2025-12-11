package gerais;
import java.util.Scanner;
public class matriz_dnv {
        public static void main(String[] args) {
            Scanner matriques = new Scanner(System.in);
    
            System.out.print("Informe o número de linhas da matriz: ");
            int linhas = matriques.nextInt();
            System.out.print("Informe o número de colunas da matriz: ");
            int colunas = matriques.nextInt();
    
            int[][] matriz = new int[linhas][colunas];
    
            System.out.println("Digite os elementos da matriz:");
            for (int i = 0; i < linhas; i++) {
                for (int j = 0; j < colunas; j++) {
                    System.out.printf("Elemento [%d][%d]: ", i, j);
                    matriz[i][j] = matriques.nextInt();
                }
            }
    
            System.out.println("\nMatriz preenchida:");
            for (int i = 0; i < linhas; i++) {
                for (int j = 0; j < colunas; j++) {
                    
                    System.out.print(matriz[i][j] + " ");
                }
                System.out.println(); 
            }
    
            matriques.close(); 
        }
    }

        /*int matriz [][] = new int [linhas][colunas];
        
            for (linhas = 0; linhas < matriz.length; linhas++) { //O for Item/linhas pergunta quantos itens tem nas linhas da matriz|| Sempre começa no zero e sempre vão ser essa estrutura do for, I e J.
                System.out.printf("\nLinha: %d| ",(linhas+1));
                for (colunas = 0; colunas < matriz [linhas].length; colunas++){ //O for Jitem/colunas pergunta quantos itens tem nas colunas da matriz. poderia ser nomeado comprimento para facilitar
                    System.out.printf("Coluna: %d| ",matriz[linhas][colunas]);*/

                      
  

