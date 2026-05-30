<?php

$conexao = mysqli_connect("localhost", "root", "", "aula_js");

$nome = $_POST["nome"];
$idade = $_POST["idade"];
$curso = $_POST["curso"];

$sql = "INSERT INTO alunos (nome, idade, curso) VALUES ('$nome', '$idade', '$curso')";

mysqli_query($conexao, $sql);

echo "aluno cadastrado com sucesso.";

?>