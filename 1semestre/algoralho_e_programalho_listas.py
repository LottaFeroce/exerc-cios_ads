# Essa é pra você, algoritmo que já devia ter sido eliminado da minha vida
# Mas ainda insiste em aparecer igual boletim no final do semestre

lista = list(range(1, 11))  # Lista padrão que todo exercício ama usar

print(f"Lista original: {lista}")

# Multiplicando tudo por 2 (pra ver se dobra a paciência também)
dobrada = [x * 2 for x in lista]
print(f"Lista dobrada (x2): {dobrada}")

# Somando 10 a cada elemento (porque a vida às vezes precisa de um boost)
somada = [x + 10 for x in lista]
print(f"Lista somada (+10): {somada}")

# Elevando ao quadrado (porque essa matéria tá ficando complexa demais)
quadrada = [x ** 2 for x in lista]
print(f"Lista ao quadrado: {quadrada}")

# Multiplicando todos os valores entre si (tentando gerar uma energia pra terminar o semestre)
from functools import reduce
import operator

produto = reduce(operator.mul, lista, 1)
print(f"Produto de todos os elementos: {produto}")

# Média dos valores (que não vai ser suficiente pra passar se depender da sorte)
media = sum(lista) / len(lista)
print(f"Média da lista: {media}")

# Segundo maior e segundo menor (os irmãos esquecidos do max e min)
ordenada = sorted(lista)
segundo_maior = ordenada[-2]
segundo_menor = ordenada[1]
print(f"Segundo maior: {segundo_maior}, Segundo menor: {segundo_menor}")

# Inversões e fatias (porque até a lista quer virar o jogo)
print(f"Lista invertida: {lista[::-1]}")
print(f"3 primeiros: {lista[:3]}, 3 últimos: {lista[-3:]}")
print(f"Posições 2 a 5: {lista[2:6]}")

# Substituições e absolutos (como quem tenta mudar de curso no meio da faculdade)
lista[0:5] = [0]*5
print(f"Primeiros 5 substituídos por 0: {lista}")

# Valor absoluto (pra limpar a negatividade dessa matéria)
lista = [-5, -3, 0, 3, 5]
absoluta = [abs(x) for x in lista]
print(f"Lista com valores absolutos: {absoluta}")

# Concatenação (porque se juntar com os outros pode ser a única salvação)
outra_lista = [10, 20, 30, 40, 50]
concatenada = lista + outra_lista
print(f"Listas concatenadas: {concatenada}")

# Remoção de duplicatas (ou como excluir o 'copiou e colou' do grupo)
lista_repetida = [1, 2, 2, 3, 4, 4, 5]
sem_duplicatas = list(set(lista_repetida))
print(f"Sem duplicatas: {sem_duplicatas}")

# Transformando números em strings (pra ver se eles contam como palavras e viram TCC)
strings = [str(num) for num in lista]
print(f"Números transformados em strings: {strings}")

# Agora chega, né? Porque nem quem montou esse exercício fez tudo isso.
print("\nResumo: você não precisa de algoritmo, você precisa é de férias.")
