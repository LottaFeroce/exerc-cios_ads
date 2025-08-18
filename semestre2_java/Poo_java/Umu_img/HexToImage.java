package Umu_img;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class HexToImage {
    public static void main(String[] args) {
        // HEX da imagem (normalmente você copiaria do ImageToHex)
        String hex = "89504E470D0A1A0A...";

        try {
            // Caminho da Área de Trabalho
            String userHome = System.getProperty("user.home");
            File pasta = new File(userHome + "\\Desktop\\imagens");
            if (!pasta.exists()) pasta.mkdirs();

            // converte hex para bytes
            byte[] bytes = hexStringToByteArray(hex);

            // salva arquivo
            File outputFile = new File(pasta, "imagem.png");
            FileOutputStream fos = new FileOutputStream(outputFile);
            fos.write(bytes);
            fos.close();

            System.out.println("Imagem salva como: " + outputFile.getAbsolutePath());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                                 + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }
}
