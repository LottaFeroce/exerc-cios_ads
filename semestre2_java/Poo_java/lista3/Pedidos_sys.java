/* import java.util.*;
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

    public void Set_nome(String nome) { this.nome = nome; }
    public String Get_nome() { return nome; }

    public String cadastrar() {
        return "Cliente " + nome + " cadastrado com sucesso";
    }

    public void atualizar() {
        System.out.println("Dados do cliente " + nome + " atualizados");
    }

    public void Consultar_pedidos() {
        System.out.println("Consultando pedidos do cliente " + nome + "...");
    }
}

class Produto {
    private int codigo;
    private String nome;
    private String descricao;
    private float preco;
    private int Quantidade_estoque;

    public void Set_nome(String nome) { this.nome = nome; }
    public String Get_nome() { return nome; }

    public void Atualizar_estoque(int Nova_quantidade) {
        Quantidade_estoque = Nova_quantidade;
        System.out.println("Estoque atualizado: " + Quantidade_estoque + " unidades.");
    }

    public void Aplicar_desconto(float percentual) {
        preco -= preco * (percentual / 100);
        System.out.println("Desconto aplicado Novo preço: R$ " + preco);
    }

    public void Exibir_informacao() {
        System.out.println("Produto: " + nome + " - " + descricao + " | R$ " + preco);
    }
}

class Pedido {
    private int id;
    private Date data;
    private int cliente;
    private float Valor_total;
    private String status;
    private List<ItemPedido> itens = new ArrayList<>();

    public void Adicionar_produto(ItemPedido item) {
        itens.add(item);
        System.out.println("Produto adicionado ao pedido");
    }

    public void Remover_produto(ItemPedido item) {
        itens.remove(item);
        System.out.println("Produto removido do pedido");
    }

    public void Calcular_total() {
        Valor_total = 0;
        for (ItemPedido item : itens) {
            Valor_total += item.Get_subtotal();
        }
        System.out.println("Valor total atualizado: R$ " + Valor_total);
    }
}

class ItemPedido {
    private int codigo;
    private String produto;
    private int cliente;
    private int quantidade;
    private float Preco_unidade;
    private float subtotal;

    public void Exibir_informacoes() {
        System.out.println("Produto: " + produto + ", Quantidade: " + quantidade +
                           ", Preço Unitário: R$ " + Preco_unidade + ", Subtotal: R$ " + subtotal);
    }

    public void Atualizar_quantidade(int novaQtd) {
        quantidade = novaQtd;
        Calcular_subtotal();
        System.out.println("Quantidade atualizada: " + quantidade);
    }

    public void Calcular_subtotal() {
        subtotal = Preco_unidade * quantidade;
    }

    public float Get_subtotal() {
        return subtotal;
    }
}

class Pagamento {
    private int codigo;
    private int pedido;
    private String Forma_pagamento;
    private float Valor_pagamento;
    private Date data;

    public void Processar_pagamento() {
        System.out.println("Pagamento processado com sucesso");
    }

    public void confirmar() {
        System.out.println("Pagamento confirmado");
    }

    public void Emitir_recibo() {
        System.out.println("Recibo emitido para o pagamento de R$ " + Valor_pagamento);
    }
}
*/