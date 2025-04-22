lista = list(range(1, 11))  

print(f"Lista original: {lista}")


dobrada = [x * 2 for x in lista]
print(f"Lista dobrada (x2): {dobrada}")

somada = [x + 10 for x in lista]
print(f"Lista somada (+10): {somada}")


quadrada = [x ** 2 for x in lista]
print(f"Lista ao quadrado: {quadrada}")


from functools import reduce
import operator

produto = reduce(operator.mul, lista, 1)
print(f"Produto de todos os elementos: {produto}")

media = sum(lista) / len(lista)
print(f"Média da lista: {media}")


ordenada = sorted(lista)
segundo_maior = ordenada[-2]
segundo_menor = ordenada[1]
print(f"Segundo maior: {segundo_maior}, Segundo menor: {segundo_menor}")


print(f"Lista invertida: {lista[::-1]}")
print(f"3 primeiros: {lista[:3]}, 3 últimos: {lista[-3:]}")
print(f"Posições 2 a 5: {lista[2:6]}")


lista[0:5] = [0]*5
print(f"Primeiros 5 substituídos por 0: {lista}")


lista = [-5, -3, 0, 3, 5]
absoluta = [abs(x) for x in lista]
print(f"Lista com valores absolutos: {absoluta}")


outra_lista = [10, 20, 30, 40, 50]
concatenada = lista + outra_lista
print(f"Listas concatenadas: {concatenada}")


lista_repetida = [1, 2, 2, 3, 4, 4, 5]
sem_duplicatas = list(set(lista_repetida))
print(f"Sem duplicatas: {sem_duplicatas}")


strings = [str(num) for num in lista]
print(f"Números transformados em strings: {strings}")


print("\nResumo: você não precisa de algoritmo, você precisa é de férias.")
