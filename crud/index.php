<?php

require_once __DIR__ . "/controllers/ProdutoController.php";

$controller = new ProdutoController();

$action = $_GET["action"] ?? "index";

switch ($action) {

    case "criar":
        $controller->criar();
        break;

    case "editar":
        $controller->editar();
        break;

    case "excluir":
        $controller->excluir();
        break;

    default:
        $controller->index();
        break;
}
