import java.util.*;

public class Pedidos_sys {
    public static void main(String[] args) {
        }
}

class Cliente {
    private int id;
    private String nome;
    private String cpf;
    private int telefone;
    private String email;

    public void setNome(String nome) { this.nome = nome; }
    public String getNome() { return nome; }

    public String cadastrar() {
        return "Cliente " + nome + " cadastrado com sucesso";
    }

    public void atualizar() {
        System.out.println("Dados do cliente " + nome + " atualizados");
    }

    public void consultarPedidos() {
        System.out.println("Consultando pedidos do cliente " + nome + "...");
    }
}

class Produto {
    private int codigo;
    private String nome;
    private String descricao;
    private float preco;
    private int quantidadeEstoque;

    public void setNome(String nome) { this.nome = nome; }
    public String getNome() { return nome; }

    public void atualizarEstoque(int novaQuantidade) {
        quantidadeEstoque = novaQuantidade;
        System.out.println("Estoque atualizado: " + quantidadeEstoque + " unidades.");
    }

    public void aplicarDesconto(float percentual) {
        preco -= preco * (percentual / 100);
        System.out.println("Desconto aplicado Novo preço: R$ " + preco);
    }

    public void exibirInformacao() {
        System.out.println("Produto: " + nome + " - " + descricao + " | R$ " + preco);
    }
}

class Pedido {
    private int id;
    private Date data;
    private int cliente;
    private float valorTotal;
    private String status;
    private List<ItemPedido> itens = new ArrayList<>();

    public void adicionarProduto(ItemPedido item) {
        itens.add(item);
        System.out.println("Produto adicionado ao pedido");
    }

    public void removerProduto(ItemPedido item) {
        itens.remove(item);
        System.out.println("Produto removido do pedido");
    }

    public void calcularTotal() {
        valorTotal = 0;
        for (ItemPedido item : itens) {
            valorTotal += item.getSubtotal();
        }
        System.out.println("Valor total atualizado: R$ " + valorTotal);
    }
}

class ItemPedido {
    private int codigo;
    private String produto;
    private int cliente;
    private int quantidade;
    private float precoUnidade;
    private float subtotal;

    public void exibirInformacoes() {
        System.out.println("Produto: " + produto + ", Quantidade: " + quantidade +
                           ", Preço Unitário: R$ " + precoUnidade + ", Subtotal: R$ " + subtotal);
    }

    public void atualizarQuantidade(int novaQtd) {
        quantidade = novaQtd;
        calcularSubtotal();
        System.out.println("Quantidade atualizada: " + quantidade);
    }

    public void calcularSubtotal() {
        subtotal = precoUnidade * quantidade;
    }

    public float getSubtotal() {
        return subtotal;
    }
}

class Pagamento {
    private int codigo;
    private int pedido;
    private String formaPagamento;
    private float valorPagamento;
    private Date data;

    public void processarPagamento() {
        System.out.println("Pagamento processado com sucesso");
    }

    public void confirmar() {
        System.out.println("Pagamento confirmado");
    }

    public void emitirRecibo() {
        System.out.println("Recibo emitido para o pagamento de R$ " + valorPagamento);
    }
}
