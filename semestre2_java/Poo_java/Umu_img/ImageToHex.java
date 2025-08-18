package Umu_img;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class ImageToHex {
    public static void main(String[] args) {
        try {
            // Caminho da Área de Trabalho
            String userHome = System.getProperty("user.home");
            File pasta = new File(userHome + "\\Desktop\\imagens");
            if (!pasta.exists()) pasta.mkdirs();

            // Arquivo de entrada
            File inputFile = new File(pasta, "nero_claudius_fate_aster_crowley");
            FileInputStream fis = new FileInputStream(inputFile);
            byte[] bytes = fis.readAllBytes();
            fis.close();

            // converte bytes para hexadecimal
            StringBuilder hex = new StringBuilder();
            for (byte b : bytes) {
                hex.append(String.format("%02X", b));
            }

            System.out.println("Hexadecimal da imagem:");
            System.out.println(hex.toString()); // cuidado: pode ser muuuito longo hehe
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
