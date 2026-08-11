<?php

print_r($_POST);



$placa = filter_input(INPUT_POST, "placa", FILTER_SANITIZE_SPECIAL_CHARS);
// $id = filter_input(INPUT_GET, "id_user" , FILTER_VALIDATE_INT);

$preco =  filter_input(INPUT_POST, "preco", FILTER_VALIDATE_INT); //VALIDAR SE VEIO UM INTEIRO


$email =  filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL); //VALIDAR SE VEIO UM INTEIRO

$descricao = $_POST['descricao'];


echo $placa . "<br>";
echo $preco . "<br>";
echo $descricao . "<br>";

echo "Email recebido: " . $email;


?>