import java.util.*;
public class Agenda_sys {
    public static void main(String[] args) {
    }
}

class Cliente {
    private String nome;
    private String cpf;
    private int telefone;
    private String email;
    private String endereco;

    public void Set_nome(String nome) { this.nome = nome; }
    public String Get_nome() { return nome; }

    public String cadastrar() {
        return "Cliente " + nome + " cadastrado com sucesso";
    }

    public void Visualizar_dados() {
        System.out.println("Nome: " + nome + ", CPF: " + cpf + ", Telefone: " + telefone +
                           ", Email: " + email + ", Endereço: " + endereco);
    }

    public void Visualizar_agendamentos() {
        System.out.println("Listando agendamentos do cliente " + nome + "...");
    }
}

class Profissional {
    private String nome;
    private String especialidade;
    private int Registro_profissional;
    private int telefone;
    private boolean disponivel;
    private List<String> horarios = new ArrayList<>();

    public void Set_nome(String nome) { this.nome = nome; }
    public String Get_nome() { return nome; }

    public boolean Verificar_disponibilidade() {
        return disponivel;
    }

    public void Adicionar_horario(String horario) {
        horarios.add(horario);
    }

    public void Remover_horario(String horario) {
        horarios.remove(horario);
    }
}

class Servico {
    private int codigo;
    private String nome;
    private String descricao;
    private int Duracao_minutos;
    private float preco;

    public void Set_nome(String nome) { this.nome = nome; }
    public String Get_nome() { return nome; }

    public float Calcular_preco() {
        return preco;
    }

    public void Atualizar_descricao(String Nova_descricao) {
        this.descricao = Nova_descricao;
    }

    public void Listar_servicos() {
        System.out.println("Serviço: " + nome + " - " + descricao + " (R$ " + preco + ")");
    }
}

class Pagamento {
    private int id;
    private float valor;
    private String formaPagamento;
    private Date data;
    private String status;

    public void processar() {
        status = "Processado";
        System.out.println("Pagamento processado com sucesso");
    }

    public void Verificar_status() {
        System.out.println("Status do pagamento: " + status);
    }

    public void Emitir_recibo() {
        System.out.println("Recibo emitido. Valor: R$ " + valor);
    }
}

class Agendamento {
    private int codigo;
    private Date data;
    private Date hora;
    private String cliente;
    private String profissional;
    private String status;

    public void Criar_agendamento() {
        status = "Agendado";
        System.out.println("Agendamento criado com sucesso");
    }

    public void cancelar() {
        status = "Cancelado";
        System.out.println("Agendamento cancelado");
    }

    public void confirmar() {
        status = "Confirmado";
        System.out.println("Agendamento confirmado");
    }
}
