package Umu_img;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
public class ImageToBin {
    public static void main(String[] args) {
        try {
            String userHome = System.getProperty("user.home");
            File pasta = new File(userHome + "\\Desktop\\imagens");
            if (!pasta.exists()) pasta.mkdirs();

            String nomeArquivo = "nero_claudius_fate_aster_crowley.png";
            File inputFile = new File(pasta, nomeArquivo);

            if (!inputFile.exists()) {
                System.out.println("O arquivo " + nomeArquivo + " não foi encontrado na pasta " + pasta.getAbsolutePath());
                return;
            }

            FileInputStream fis = new FileInputStream(inputFile);
            byte[] bytes = fis.readAllBytes();
            fis.close();

            File outputFile = new File(pasta, "imagem.bin");
            FileOutputStream fos = new FileOutputStream(outputFile);
            fos.write(bytes);
            fos.close();

            System.out.println("Imagem convertida para binário com sucesso: " + outputFile.getAbsolutePath());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
