'''create database seu_jao;
use seu_jao;

select * from clientes;
select * from comissoes;
select * from itens_venda;
select * from movimentacoes_estoque;
select * from parcelas_crediario;
select * from produtos;
select * from usuarios;
select * from vendas;
select * from vendedores;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_barras VARCHAR(50) UNIQUE,
    descricao VARCHAR(100) NOT NULL,
    categoria ENUM('Elétrico', 'Hidráulico', 'Ferragens', 'Material Básico', 'Outros') NOT NULL,
    unidade_medida ENUM('UN', 'KG', 'M', 'M²', 'CX', 'SC') NOT NULL,
    preco_custo DECIMAL(10,2) NOT NULL,
    preco_venda DECIMAL(10,2) NOT NULL,
    estoque_atual DECIMAL(10,3) NOT NULL DEFAULT 0,
    estoque_minimo DECIMAL(10,3) NOT NULL DEFAULT 0,
    estoque_maximo DECIMAL(10,3),
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('PF', 'PJ') NOT NULL,
    cpf_cnpj VARCHAR(20) UNIQUE,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco TEXT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_admissao DATE,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    vendedor_id INT,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10,2) NOT NULL,
    desconto DECIMAL(10,2) DEFAULT 0,
    forma_pagamento ENUM('Dinheiro', 'Cartão Débito', 'Cartão Crédito', 'PIX', 'Boleto', 'Crediário') NOT NULL,
    status ENUM('Concluída', 'Cancelada', 'Orçamento') DEFAULT 'Concluída',
    observacoes TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);

CREATE TABLE itens_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade DECIMAL(10,3) NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES vendas(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TABLE parcelas_crediario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT NOT NULL,
    numero_parcela INT NOT NULL,
    valor_parcela DECIMAL(10,2) NOT NULL,
    data_vencimento DATE NOT NULL,
    data_pagamento DATE,
    status ENUM('Pendente', 'Pago', 'Atrasado') DEFAULT 'Pendente',
    FOREIGN KEY (venda_id) REFERENCES vendas(id) ON DELETE CASCADE
);

CREATE TABLE comissoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT NOT NULL,
    vendedor_id INT NOT NULL,
    valor_comissao DECIMAL(10,2) NOT NULL,
    data_calculo DATE NOT NULL,
    status ENUM('Pendente', 'Pago') DEFAULT 'Pendente',
    FOREIGN KEY (venda_id) REFERENCES vendas(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);

CREATE TABLE movimentacoes_estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    tipo ENUM('Entrada', 'Saída', 'Ajuste') NOT NULL,
    quantidade DECIMAL(10,3) NOT NULL,
    origem VARCHAR(50) COMMENT 'Venda, Compra, Ajuste, etc',
    origem_id INT COMMENT 'ID do documento de origem',
    data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(50),
    observacoes TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    perfil ENUM('Administrador', 'Gerente', 'Vendedor') NOT NULL,
    vendedor_id INT,
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);

CREATE INDEX idx_produtos_descricao ON produtos(descricao);
CREATE INDEX idx_vendas_data ON vendas(data_venda);
CREATE INDEX idx_vendas_cliente ON vendas(cliente_id);
CREATE INDEX idx_vendas_vendedor ON vendas(vendedor_id);
CREATE INDEX idx_itens_venda_produto ON itens_venda(produto_id);
CREATE INDEX idx_movimentacoes_produto ON movimentacoes_estoque(produto_id);'''