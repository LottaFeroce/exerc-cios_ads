<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Editar Produto</title>
</head>

<body>

    <h1>Editar Produto</h1>

    <?php if (isset($erro)): ?>

        <p>
            <?= htmlspecialchars($erro) ?>
        </p>

    <?php endif; ?>

    <form method="POST">

        <label>
            Nome:
        </label>

        <br>

        <input
            type="text"
            name="nome"
            value="<?= htmlspecialchars($produto["nome"]) ?>"
            required
        >

        <br><br>

        <label>
            Descrição:
        </label>

        <br>

        <textarea name="descricao"><?= htmlspecialchars(
            $produto["descricao"]
        ) ?></textarea>

        <br><br>

        <label>
            Preço:
        </label>

        <br>

        <input
            type="number"
            name="preco"
            step="0.01"
            min="0"
            value="<?= $produto["preco"] ?>"
            required
        >

        <br><br>

        <label>
            Quantidade:
        </label>

        <br>

        <input
            type="number"
            name="quantidade"
            min="0"
            value="<?= $produto["quantidade"] ?>"
            required
        >

        <br><br>

        <button type="submit">
            Atualizar
        </button>

    </form>

    <br>

    <a href="index.php">
        Voltar
    </a>

</body>

</html>
