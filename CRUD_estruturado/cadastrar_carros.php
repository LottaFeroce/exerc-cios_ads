<?php

include 'conexao.php';
// DEBUG PARA SABER O QUE TEMOS NO POST
//print_r($_POST);

if( isset($_POST['cadastrar']) ){

    $marca = $_POST['marca'];
    $modelo = $_POST['modelo'];
    $placa = $_POST['placa'];
    $cor = $_POST['cor'];
    $ano = $_POST['ano'];
    $km_rodado = $_POST['km'];

    $sql = "INSERT INTO carro (marca,modelo,placa,cor,ano,km_rodados) 
    VALUES ('$marca', '$modelo', '$placa', '$cor', '$ano', '$km_rodado')";

    $res = mysqli_query($conn, $sql);

    if($res){
        echo "CADASTRADO COM SUCESSO!!";
    }else{
        echo "ERROR";
    }  
}