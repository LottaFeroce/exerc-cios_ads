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

"""6 – Um comerciante possui uma loja de artigos de R$ 1,99. Para
agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu
uma tabela que contém o número de itens que o cliente comprou e ao
lado o valor da conta. Desta forma a atendente do caixa precisa apenas
contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver uma função que monta esta
tabela de preços, que conterá os preços de 1 até 50 produtos,
conforme o exemplo abaixo:

def loja_artigometro():
    valor_original = 1.99
    for item in range(1, 51):
        total = item * valor_original
        print(f"{item} - R$ {total:.2f}")

loja_artigometro()
"""

"""7 – Crie uma função que efetue o cálculo do salário e
como retorno teremos o valor a ser pago conforme o
número de horas trabalhadas. Considere a carga
horária de 40h por semana como salário base, caso
ultrapasse o limite de 40h, o funcionário deve receber
50% a mais por hora excedente.

def salariometro():
    salario_base = float(input("Digite o seu salário base semanal (para 40h): R$ "))
    horario_eleitoral_obrigatorio = float(input("Informe o número de horas trabalhadas na semana: "))

    valor_hora = salario_base / 40

    if horario_eleitoral_obrigatorio <= 40:
        salario_total = valor_hora * horario_eleitoral_obrigatorio
    else:
        horas_extras = horario_eleitoral_obrigatorio - 40
        salario_total = salario_base + (horas_extras * valor_hora * 1.5)

    print(f"Salário a receber: R$ {salario_total:.2f}")

salariometro()
"""

'''8 – Um pescador, comprou um PC para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar
uma multa de R$ 4,00 por quilo excedente. O pescador precisa que
você crie uma função para ler a quantidade de peixes e calcular o
excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que o pescador deverá
pagar. Imprima os dados do programa com as mensagens adequadas.
def Go_fish():
    limite_kg = 50
    multa_kg_excedente = 4.00

    peso_peixes = float(input("Digite o peso total de peixes pescados (em Kg): "))

    if peso_peixes > limite_kg:
        excesso = peso_peixes - limite_kg
        multa = excesso * multa_kg_excedente
    else:
        excesso = 0
        multa = 0

    print(f"\nRelatório da Pesca:\nPeso total pescado: {peso_peixes:.2f} Kg\nExcesso de peso: {excesso:.2f} Kg\nMulta a pagar: R$ {multa:.2f}")
Go_fish()'''

"""9 – O gestor de uma rede de shoppings, precisa contratar um
sistema para administrar o estacionamento, a principal função do
sistema é calcularTempo(). Considere o valor mínimo de R$9,00
por hora e R$ 1,50 por hora adicional. O principal argumento da
função é o tempo utilizado em minutos, a função deve retornar o
valor total. Caso o usuário fique no estacionamento por menos de
15 minutos, o tempo utilizado não será cobrado
def extorsao_shopping(tempo_minutos):
    valor_minimo = 9.00  
    hora_adicional = 1.50  
    
   
    if tempo_minutos < 15:
        return 0.00
    
 
    tempo_em_horas = tempo_minutos / 60
    
    if tempo_em_horas <= 1:
       
        return valor_minimo
    else:
      
        horas_adicionais = tempo_em_horas - 1  
        valor_adicional = horas_adicionais * hora_adicional
        return valor_minimo + valor_adicional

# Exemplo de uso:
tempo = float(input("Digite o tempo de permanência no estacionamento (em minutos): "))
valor_total = extorsao_shopping(tempo)
print(f"Valor total a pagar: R$ {valor_total:.2f}")
"""
'''10 – Adicione na função calcularTempo() do sistema para
estacionamento o valor dos impostos pago pelo cliente. Considere
o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o
recibo do cliente de acordo com a saída abaixo:

def calcularTempo():
    print("=== SISTEMA DE ESTACIONAMENTO ===")
    
    entrada = int(input("Digite a hora de entrada (0-23): "))
    saida = int(input("Digite a hora de saída (0-23): "))
    
    preco_hora = 5.00


    if saida < entrada:
        tempo = (24 - entrada) + saida
    else:
        tempo = saida - entrada

    tempo = max(1, tempo) 

    valor_base = tempo * preco_hora
    pis = valor_base * 0.0033
    cofins = valor_base * 0.0020
    icms = valor_base * 0.17

    total = valor_base + pis + cofins + icms
    print(f"\n=== RECIBO DE PAGAMENTO ===\nTempo estacionado: {tempo} hora(s)\nValor por hora: R$ {preco_hora:.2f}\nValor base: R$ {valor_base:.2f}\nPIS (0,33%): R$ {pis:.2f}\nCOFINS (0,20%): R$ {cofins:.2f}\nICMS (17%): R$ {icms:.2f}\nTotal a pagar: R$ {total:.2f}\n===============================")
calcularTempo()'''

"""11 – Uma pessoa está interessada em comprar um carro e deseja fazer um
financiamento. Ela tem uma quantia X para dar de entrada, uma taxa de juros é
definida pelo banco e a pessoa pode escolher o número de parcelas que deseja
financiar.
Crie uma função que simule um financiamento, levando em consideração o regime de
juros compostos. O programa deve solicitar ao usuário o valor do veiculo, o valor da
entrada, a taxa de juros e a quantidade de parcelas. Além disso, o programa deve
exibir o valor total pago, a quantia dos juros pagos e o valor de cada parcela. O
programa deve apresentar as informações de forma clara e objetiva, facilitando a
compreensão por parte do usuário.
def simularFinanciamento():
    print("=== SIMULADOR DE FINANCIAMENTO DE VEÍCULO ===")

  
    valor_veiculo = float(input("Informe o valor do veículo (R$): "))
    entrada = float(input("Informe o valor da entrada (R$): "))
    taxa_juros = float(input("Informe a taxa de juros mensal (%): "))
    parcelas = int(input("Informe a quantidade de parcelas: "))

   
    valor_financiado = valor_veiculo - entrada
    taxa_decimal = taxa_juros / 100

    
    montante = valor_financiado * (1 + taxa_decimal) ** parcelas

    valor_parcela = montante / parcelas
    juros_pagos = montante - valor_financiado

  
    print(f"\n=== DETALHES DO FINANCIAMENTO ===\nValor do veículo: R$ {valor_veiculo:,.2f}\nEntrada: R$ {entrada:,.2f}\nValor financiado: R$ {valor_financiado:,.2f}\nTaxa de juros mensal: {taxa_juros:.2f}%\nNúmero de parcelas: {parcelas}\nValor de cada parcela: R$ {valor_parcela:,.2f}\nTotal pago ao final: R$ {montante:,.2f}\nTotal de juros pagos: R$ {juros_pagos:,.2f}\n==========================================")
"""
