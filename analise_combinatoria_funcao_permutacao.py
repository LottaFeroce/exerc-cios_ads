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

(0 ao 9 senha para cartão  10*10*10*10 10^4 = 10.000 -> isso com os números repetindo na senha )

"""