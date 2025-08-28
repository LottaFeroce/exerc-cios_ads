'''1 def produto(numero1: int, numero2: int, numero3: int):
    resultado = numero1 * numero2 * numero3
    return resultado

print("O resultado é:", produto(2, 3, 2))
'''

'''2 def exponencia (numero1: int,numero2: int):
    resultado = (numero1 ** numero2 )
    return resultado
print("O resultado é:",exponencia(2,3))'''

"""3 def quantidade():
    tam = input("Digite algo: ")
    tamanho = len(tam)
    return tamanho

print("Quantidade de itens digitados:", quantidade())"""

'''4 def positivo_negativo():
    numero = int(input("Informe um número positivo ou negativo: "))
    
    if numero < 0:
        print("Negativo")
        return "Negativo"
    else:
        print("Positivo")
        return "Positivo"

print("O valor é", positivo_negativo())'''

'''5 Escreva um programa com uma função chamada
somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item
antes do imposto. A função “altera” o valor de custo para
incluir o imposto sobre vendas. Por fim deve retornar o novo
valor para o usuário considerando o percentual do imposto
def somaImposto(taxaImposto: float, custo: float) -> float:
    reajuste = custo + (custo * (taxaImposto / 100))
    return reajuste
custo = float(input("Informe o valor do produto antes do imposto: "))
taxa = float(input("Informe a taxa de imposto em %: "))
valor_final = somaImposto(taxa, custo)
print(f"O valor pré-imposto era: R${custo:.2f}")
print(f"Após aplicar {taxa:.2f}% de imposto, o valor ficou: R${valor_final:.2f}")
'''
