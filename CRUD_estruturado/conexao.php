<?php

$local = "localhost";
$user = "root";
$password = "";
$banco = "garage";

$conn = new mysqli($local,$user,$password,$banco);

if($conn){
    //echo "Conectado com sucesso!";
}
else{
    echo "ERROR";
}