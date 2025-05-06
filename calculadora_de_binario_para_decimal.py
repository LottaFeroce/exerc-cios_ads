#Binário para Decimal 
import os 
value = input("\nDigite o número em Binário: ")
decimal_value =[]
validate = len(value)

for iteration in value:
    validate = validate - 1
    if iteration == "1":
        elevacao = 2 ** validate
        decimal_value.append(elevacao)
print("\n","Decimais:",decimal_value,"\n","Decimal",sum(decimal_value))