pessoa = {"nome":"skibidi",
          "idade":21,
          "cidade":"CG"}
def verificar_cidade(dicionario:dict):
    if dicionario["cidade"] == "CG":
        return "É de Campo Grande"
    else:
        return f"É de {dicionario["cidade"]}"
    
cidade_skibidi = verificar_cidade(pessoa)
print(cidade_skibidi)

def imprime_listas(lista):
    for item in lista:
        print(item)