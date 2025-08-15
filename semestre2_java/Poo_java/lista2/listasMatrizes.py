item = 0
jitem = 0
matriz = []
lin = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))
while item < lin:
    linha=[]
    while jitem < colunas:
        numero = 10
        linha.append(numero)
        jitem = jitem +1
    matriz.append(linha)
    item = item + 1
    jitem = 0
print(matriz)