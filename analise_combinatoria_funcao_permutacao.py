"""
fatoração (n!) é o produto de todos os números naturais positivos até n

permutação considera a ordem e usa a fatoração para calcular as possibilidades

diferenciar permutação de combinação é crucial, pois a ordem dos elementos altera o resultado na permutação.

exc:.. 40 alunos 3 lideres
1º 2º 3º ordem importa, |onde a ordem importa não se faz combinação, se faz permutação|logo o contrario se faz combinação|



permutação se utiliza fatoração.
em permutações simples consideramos todos os elementos em todos os...(trocou de slide)
numero de elementos é igual ao numero posições usa fatoração,

equação de arranjo= An,p=n!/(n*p)!

Arranjo |6 possibilidades 1,2,3|
40!=59280
40*39*38=59280
A40,3=40!/(40-3)! = 40!/37!=59280

combinação
C=n!/P!*(n-p)!
C=40!/3!(40-3)!
C=40*39*38*37/3!-37!-(-cortado-)=40*39*38/6=9880
40!=40*39*38*37*36*35!=40!/36!=40*39*38*37*-36!-/-36!-=40*39*38*37*

anagrama
P^x=N!/n!

aula = P=N!/n! = 4!/2!=4*3*-2!-/-2!- =12

paralelepipedo
p=3
a=2
l=2
e=3
p^p,a,l,e= n!/p!*a!*l!*e! = 14!/3!*2!*2!3!=87178291200/144=605.404.800


1)Quantas senhas com 4 algarismos diferentes podemos escrever com os algarismos 1,2,3,4,5,6,7,8 e 9?
arranjo:
An,p=N!/(n-p)! = 9!/(9-4)!=9!/5! = 9*8*7*6*-5!-/-5!- =A9,4=9*8*7*6=3024
9*8*7*6
n=p=N!  

(0 ao 9 senha para cartão  10*10*10*10 = 10^4 = 10.000 -> isso com os números repetindo na senha)

12)certa lanchonete possui 5 funcionarios para atender os clientes durante os diasda semana
R=C(5,1)+C(5,2)+(5,3)+(5,4)+(5,5) = 5+10+10+5+1
            5!/2!(5-2)!=5!/2!3!=5*-4*3!-/-2!3!-

13)A secretáia de um médico precisa agendar quatro pacientes, a,  b, c, e d, para um mesmo dia.
Os pacientes A e B não podem ser agendados no periodo da manhã e o paciente C não pode ser agendado no periodo da tarde.
Sabendo que para esse dia estão disponiveis 3 horários no mesmo periodo da manhã e 4 no periodo da tarde, 
o número de maneiras distintas de a secretária agendar esses pacientes é?
R:D)144

permutação simples? 3!*4!? Sim!(talvez?) 3!*4!=144

M manhã| T tarde
1°m c d c d         |ficticio m: c d, t: a b
2°m d c     d c
3°m     d c c d

1°t a a b
2°t b d d
3°t d b a
4°t 

arranjo A=N!/(n-p)!
A(3,2)*A(4,2)
A(3,1)*A(4,3)

A(3,2)=3!/(3-2)!=3!/1!=6
A(4,2)=4!/2!=4*3*-2!-/-2!- = 12
A(3,1)=3!/2!=3*-2!-/-2!- =3
A(4,3)=4!/1!=24

A(3,2)*A(4,2)=6*12=72
A(3,1)*A(4,3)=3*24=72
R=72+72=144

E= multiplicar Ou= soma
==========================================
Teorema de Bayes
P(A|B)=P(B|A)P(A)/P(B)

P=probabilidade
A=estar contaminado
B=Exame positivo

teste=90% acurácia
1000 pessoas = 1% tem h1n1

1% de 1000 = 10
10 tem h1n1
990 não tem h1n1

resultado do teste:
    891 acertou
990<
    89 errou
                > 99+9=108 probabilidade: P=9/108=83%
    9 acertou
10<
    1 errou

 P(B)=P=(B|A)*P(A)+P(B|Â)*P(Â)
    0.90 * 0.01 + 0.10 * 0.99

    P(A|B) = 0.90*0.01/0.9*0.01+0.10*0.99=83%
"""