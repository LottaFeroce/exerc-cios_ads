<?php

require_once __DIR__ . "/../config/Database.php";

class Produto
{
    private PDO $db;

    public function __construct()
    {
        $this->db = Database::getConnection();
    }

    public function listar(): array
    {
        $sql = "SELECT * FROM produtos ORDER BY id DESC";

        $stmt = $this->db->query($sql);

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function buscarPorId(int $id): ?array
    {
        $sql = "SELECT * FROM produtos WHERE id = :id";

        $stmt = $this->db->prepare($sql);

        $stmt->execute([
            ":id" => $id
        ]);

        $produto = $stmt->fetch(PDO::FETCH_ASSOC);

        return $produto ?: null;
    }

    public function criar(
        string $nome,
        string $descricao,
        float $preco,
        int $quantidade
    ): bool {

        $sql = "INSERT INTO produtos
                (nome, descricao, preco, quantidade)
                VALUES
                (:nome, :descricao, :preco, :quantidade)";

        $stmt = $this->db->prepare($sql);

        return $stmt->execute([
            ":nome" => $nome,
            ":descricao" => $descricao,
            ":preco" => $preco,
            ":quantidade" => $quantidade
        ]);
    }

    public function atualizar(
        int $id,
        string $nome,
        string $descricao,
        float $preco,
        int $quantidade
    ): bool {

        $sql = "UPDATE produtos
                SET nome = :nome,
                    descricao = :descricao,
                    preco = :preco,
                    quantidade = :quantidade
                WHERE id = :id";

        $stmt = $this->db->prepare($sql);

        return $stmt->execute([
            ":id" => $id,
            ":nome" => $nome,
            ":descricao" => $descricao,
            ":preco" => $preco,
            ":quantidade" => $quantidade
        ]);
    }

    public function excluir(int $id): bool
    {
        $sql = "DELETE FROM produtos WHERE id = :id";

        $stmt = $this->db->prepare($sql);

        return $stmt->execute([
            ":id" => $id
        ]);
    }
}
