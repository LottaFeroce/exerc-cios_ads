<?php 
class cliente{
    public string $nome;
    public string $email;
    public string $senha;
    public string $contato;
}
class conta{
    public int $numero;
    public string $tipo;
    public float $valor;
}

$cliente = new cliente();
$conta = new conta();
$cliente ->nome = 'Nomeraldo Silva';
$conta ->valor = 6739.00;
?>

<?php include 'includes/header.php';?>
<p>Nome: <?= $cliente->nome?></p>
<p>Valor: <?= $conta->valor?></p>
<?php include 'includes/footer.php';?>