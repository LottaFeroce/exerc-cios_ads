<?php
include 'conexao.php';

$id = $_GET['id'];
$sql = "SELECT * FROM carro WHERE id_carro=$id";
$res = mysqli_query($conn, $sql);
$carro = mysqli_fetch_assoc($res); //CONVERTEU O OBJ SQL EM ARRAY DO PHP

// print_r($carro);
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
        Edição de Carro
    </h1>
    <form method="POST">

        <input type="text" name="marca" id="marca" value="<?=$carro['marca']?>">
        <input type="text" name="modelo" id="modelo"  value="<?=$carro['modelo']?>">
        <input type="text" name="placa" id="placa"  value="<?=$carro['placa']?>">
        <input type="text" name="cor" id="cor"  value="<?=$carro['cor']?>">
        <input type="text" name="ano" id="ano"  value="<?=$carro['ano']?>">
        <input type="text" name="km" id="km"  value="<?=$carro['km_rodados']?>">
        
        <input type="submit" name="editar" value="Salvar">
    </form>
</body>
</html>