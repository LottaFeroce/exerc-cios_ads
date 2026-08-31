<?php

require_once __DIR__ . "/../models/Produto.php";

class ProdutoController
{
    private Produto $produto;

    public function __construct()
    {
        $this->produto = new Produto();
    }

    public function index(): void
    {
        $produtos = $this->produto->listar();

        require __DIR__ . "/../views/produtos/index.php";
    }

    public function criar(): void
    {
        if ($_SERVER["REQUEST_METHOD"] === "POST") {

            $nome = trim($_POST["nome"] ?? "");
            $descricao = trim($_POST["descricao"] ?? "");
            $preco = (float) ($_POST["preco"] ?? 0);
            $quantidade = (int) ($_POST["quantidade"] ?? 0);

            if ($nome === "" || $preco < 0 || $quantidade < 0) {
                $erro = "Preencha os dados corretamente.";

                require __DIR__ . "/../views/produtos/criar.php";
                return;
            }

            $this->produto->criar(
                $nome,
                $descricao,
                $preco,
                $quantidade
            );

            header("Location: index.php");
            exit;
        }

        require __DIR__ . "/../views/produtos/criar.php";
    }

    public function editar(): void
    {
        $id = filter_input(
            INPUT_GET,
            "id",
            FILTER_VALIDATE_INT
        );

        if (!$id) {
            header("Location: index.php");
            exit;
        }

        $produto = $this->produto->buscarPorId($id);

        if (!$produto) {
            echo "Produto não encontrado.";
            return;
        }

        if ($_SERVER["REQUEST_METHOD"] === "POST") {

            $nome = trim($_POST["nome"] ?? "");
            $descricao = trim($_POST["descricao"] ?? "");
            $preco = (float) ($_POST["preco"] ?? 0);
            $quantidade = (int) ($_POST["quantidade"] ?? 0);

            if ($nome === "" || $preco < 0 || $quantidade < 0) {
                $erro = "Preencha os dados corretamente.";

                require __DIR__ . "/../views/produtos/editar.php";
                return;
            }

            $this->produto->atualizar(
                $id,
                $nome,
                $descricao,
                $preco,
                $quantidade
            );

            header("Location: index.php");
            exit;
        }

        require __DIR__ . "/../views/produtos/editar.php";
    }

    public function excluir(): void
    {
        if ($_SERVER["REQUEST_METHOD"] !== "POST") {
            header("Location: index.php");
            exit;
        }

        $id = filter_input(
            INPUT_POST,
            "id",
            FILTER_VALIDATE_INT
        );

        if ($id) {
            $this->produto->excluir($id);
        }

        header("Location: index.php");
        exit;
    }
}

