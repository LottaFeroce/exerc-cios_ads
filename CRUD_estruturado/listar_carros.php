<?php
include 'conexao.php';

$sql = "SELECT * FROM carro";
$res = mysqli_query($conn, $sql);
//OBJETO SQL
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
        Listagem de Carros
    </h1>
    
    <table>
        <thead>
            <th>Id</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Placa</th>
            <th>Cor</th>
            <th>Ano</th>
            <th>Editar</th>
            <th>Excluir</th>
        </thead>

        <tbody>
        <?php
            if($res){
                while($row = $res->fetch_assoc()){
                    echo '
                        <tr>
                            <td> '.$row["id_carro"].' </td>
                            <td> '.$row["marca"].' </td>
                            <td> '.$row["modelo"].' </td>
                            <td>'.$row["placa"].' </td>
                            <td> '.$row["cor"].' </td>
                            <td> '.$row["ano"].' </td>
                            <td> <a href="editar_carros.php?id='.$row["id_carro"].'"> Editar </a> </td>
                            <td> <a href="excluir_carros.php?id='.$row["id_carro"].'"> Excluir </a> </td>
                             
                        </tr>
                    ';
                }
            }
        ?>
        </tbody>
    </table>
</body>
</html>