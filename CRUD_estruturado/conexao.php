<?php

$local = "localhost";
$user = "remoto";
$password = "12345";
$banco = "garage";

$conn = new mysqli($local,$user,$password,$banco);

if($conn){
    //echo "Conectado com sucesso!";
}
else{
    echo "ERROR";
}