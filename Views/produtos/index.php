<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Produtos</title>
</head>

<body>

    <h1>Cadastro de Produtos</h1>

    <a href="index.php?action=criar">
        Cadastrar produto
    </a>

    <br><br>

    <table border="1" cellpadding="8">

        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Descrição</th>
            <th>Preço</th>
            <th>Quantidade</th>
            <th>Ações</th>
        </tr>

        <?php foreach ($produtos as $produto): ?>

            <tr>

                <td>
                    <?= $produto["id"] ?>
                </td>

                <td>
                    <?= htmlspecialchars($produto["nome"]) ?>
                </td>

                <td>
                    <?= htmlspecialchars($produto["descricao"]) ?>
                </td>

                <td>
                    R$ <?= number_format(
                        $produto["preco"],
                        2,
                        ",",
                        "."
                    ) ?>
                </td>

                <td>
                    <?= $produto["quantidade"] ?>
                </td>

                <td>

                    <a href="index.php?action=editar&id=<?= $produto["id"] ?>">
                        Editar
                    </a>

                    <form
                        method="POST"
                        action="index.php?action=excluir"
                        style="display:inline;"
                    >

                        <input
                            type="hidden"
                            name="id"
                            value="<?= $produto["id"] ?>"
                        >

                        <button type="submit">
                            Excluir
                        </button>

                    </form>

                </td>

            </tr>

        <?php endforeach; ?>

    </table>

</body>

</html>

