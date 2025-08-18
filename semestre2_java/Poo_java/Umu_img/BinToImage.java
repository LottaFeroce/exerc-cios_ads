package Umu_img;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
public class BinToImage {
    public static void main(String[] args) {
        try {
            String userHome = System.getProperty("user.home");
            File pasta = new File(userHome + "\\Desktop\\imagens");

            File inputFile = new File(pasta, "imagem.bin");
            if (!inputFile.exists()) {
                System.out.println("O arquivo binário não foi encontrado: " + inputFile.getAbsolutePath());
                return;
            }
            FileInputStream fis = new FileInputStream(inputFile);
            byte[] bytes = fis.readAllBytes();
            fis.close();
            File outputFile = new File(pasta, "Emperor_umu.png");
            FileOutputStream fos = new FileOutputStream(outputFile);
            fos.write(bytes);
            fos.close();
            System.out.println("Imagem reconstruída com sucesso: " + outputFile.getAbsolutePath());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
