#Decimal para binário
import os
"""decimal=[]
value = 29
new_value = value % 2
print(new_value)
value = value//2
print(value)
decimal.insert(0,new_value)
print(decimal)"""
value = float(input("Digite um valor em decimal para converter para binário: "))
binary_value = []
while value > 0:
    new_value = value % 2
    new_value = int(new_value)
    print("Resto: ",new_value)
    value = value//2
    print("Dividendo: ",value)
    value =int(value)
    binary_value.insert(0,new_value)
    print("\nBinário","".join(map(str,binary_value)))
print("\n","Valor em Binário:",binary_value,'\n',"Valor:",value)