"""1) q>1e0<q<1: Crescente

2)q>1e0<q<1: Decrescente

q>1 e seus termos são negativos; exemplo (-1,-3,-9)
0<q<1 e seus termos positivos;(2,2/[slide-passou])

3)q<0:Alternante 
Uma PG é alternante quando a sua razão for menor que zero;
exemplo (5,-50,500,...)

4)q=1: Constante 
Uma PG é constante quando a razão q for igual a um; (9,9,9,...)

formula do termo geral de uma pg

an=a1*q^1n-1

formula da soma dos termos de uma pg
Sn=a1(1-q^n)/1-q

produto dos termos de uma pg
Pg=a1^n*q*n*(n-1)/2
"""
import time
import math
def progressao_geometrica(termo1,fator_mult,tamanho):
    resultado = termo1
    inicio = time.time()
    resultado = termo1*fator_mult**(tamanho-1)
    end = time.time()
    tempo = end - inicio
    print("\nTempo percorrido :",tempo,"Segundos")
    return resultado
    

def soma_pg_finita(termo1,fator_mult,tamanho):
    return (termo1*(1-fator_mult**tamanho)/(1-fator_mult))

def soma_pg_infinita(termo1,fator_mult):
    return (termo1/(termo1-fator_mult))

def produto_do_termo(termo1,fator_mult,tamanho):
    return (termo1**(tamanho))*fator_mult**(tamanho*(tamanho-1)/2)

def progressao_geometrica_evil(termo1,fator_mult,resultado):
    tamanho = (math.log(resultado,10)/(math.log(termo1*fator_mult,10)))+1
    return tamanho

def progressao_geometrica_evil_mais_mais(termo1,fator_mult,resultado):
    tamanho = (math.log((resultado/termo1)/fator_mult)+1)
    return tamanho
"""
#                          numero/termo|razão|tamanho
print(progressao_geometrica(8, -6, 10))
print(soma_pg_finita(5, 0.2, 100))
print(soma_pg_infinita(5, 0.2))
print(produto_do_termo(5,1,10))
"""

#exercicio_1
#print(progressao_geometrica(1,2,11))
#exercicio_1
#print(soma_pg_finita(1,2,11))

#exercicio_2
# for i in range(1,15):
#print("Dia:",i,"Quantidade:",progressao_geometrica(1,2,i))
#print("Dia;",progressao_geometrica_evil(1,2,1024))

#exercicio_3
#for i in range(1,15):
#    print(-3**(-i))

#exercicio_4
print("Termo:",progressao_geometrica_evil(100,2,3200))
tempo=0
for i in range(1,7):
    print(progressao_geometrica(100,2,i))
    tempo+=20
print("Tempo:",tempo)