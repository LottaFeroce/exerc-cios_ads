package gerais;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
public class user {

    private String nome;
    private String email;
    private String senha;
    private boolean ativo;   
    public user(String nome, String email, String senha, boolean ativo) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.ativo = ativo;
    }

    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getSenha() {
        return senha;
    }
    public void setSenha(String senha) {
        this.senha = senha;
    }
    public boolean isAtivo() {
        return ativo;
    }
    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }   
    public boolean realizarLogin(String email, String senha) {
        return this.email.equals(email) &&
               this.senha.equals(senha) &&
               this.ativo; 
    }

    
    public static void salvarUsuarios(ArrayList<user> usuarios) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("usuarios.txt"))) {
            for (user u : usuarios) {
                writer.write(u.getNome() + ";" + u.getEmail() + ";" + u.getSenha() + ";" + u.isAtivo() + "\n");
            }
        } catch (IOException e) {
            System.out.println("Erro ao salvar os usuários: " + e.getMessage());
        }
    }

    
    public static ArrayList<user> carregarUsuarios() {
        ArrayList<user> usuarios = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("usuarios.txt"))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                String[] dados = linha.split(";");
                String nome = dados[0];
                String email = dados[1];
                String senha = dados[2];
                boolean ativo = Boolean.parseBoolean(dados[3]);
                usuarios.add(new user(nome, email, senha, ativo));
            }
        } catch (IOException e) {
            System.out.println("Erro ao carregar os usuários: " + e.getMessage());
        }
        return usuarios;
    }

    
    public static void main(String[] args) {
        
        ArrayList<user> usuarios = carregarUsuarios();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nMENU:");
            System.out.println("1 - Login");
            System.out.println("2 - Cadastro de novo usuário");
            System.out.println("3 - Listar usuários cadastrados");
            System.out.println("4 - Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); 

            if (opcao == 1) {
           
                System.out.print("Digite seu email: ");
                String emailInput = scanner.nextLine();
                System.out.print("Digite sua senha: ");
                String senhaInput = scanner.nextLine();

                boolean loginRealizado = false;
                for (user u : usuarios) {
                    if (u.realizarLogin(emailInput, senhaInput)) {
                        System.out.println("Login bem-sucedido! Bem-vindo(a), " + u.getNome() + ".");
                        loginRealizado = true;
                        break;
                    }
                }

                if (!loginRealizado) {
                    System.out.println("\nEmail/senha incorretos ou usuário inativo.");
                }

            } else if (opcao == 2) {

                System.out.print("Digite o nome: ");
                String nome = scanner.nextLine();
                System.out.print("Digite o email: ");
                String email = scanner.nextLine();
                System.out.print("Digite a senha: ");
                String senha = scanner.nextLine();
                System.out.print("Usuário está ativo? (true/false): ");
                boolean ativo = scanner.nextBoolean();
                scanner.nextLine(); 
                usuarios.add(new user(nome, email, senha, ativo));
                System.out.println("Usuário cadastrado com sucesso!");
                salvarUsuarios(usuarios);

            } else if (opcao == 3) {
                                System.out.println("\nUsuários cadastrados:");
                for (user u : usuarios) {
                    System.out.println("Nome: " + u.getNome() + " | Email: " + u.getEmail() + " | Status: " + (u.isAtivo() ? "Ativo" : "Inativo"));
                }
            } else if (opcao == 4) {
                
                System.out.println("Saindo...");
                break;
            } else {
                System.out.println("Opção inválida! Tente novamente.");
            }
        }
        scanner.close();
    }
}
