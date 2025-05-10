"""
Em relação aos sinais, podem-se destacar as seguintes definições e considerações iniciais:
Sinal: entidade que carrega informação
(slide passou)


Os circuitos digitais ou circuitos lógicos são definidos como circuitos eletrônicos que empregam a utilização(slide passou)

Álgebra de Booleana:
Y= XOR (A,B) = A + B = (Não ¬ A)¬AB + A¬B(Não ¬ B)
Y = XNOR (A,B) = A*B = AB +¬A¬B

exemplos 
1-() A.B+C'
2-NOT (A.B+C)'
3-AND A.(B+C)'
4-OR A.(B+C)'

Name         AND form(E)   OR form(OU)
Identity law |1*A = A|0 + A = A
Null law|0*A = 0| 1 + A = 1
Idempotent law|A*A = A |A + A = A
Inverse law|A*¬A = 0|A+¬A=1
Commutative law|A*B=BA|A+B=B+A
Associative law|(AB)*C =A*(BC)|(A+B)+C = A+(B+C)
Distributive law|A+BC = (A+B)*(A+C)|A(B+C=AB+AC
Aborption law|A*(A+B)=A|A+AB=A
De Morgan's law|¬A¬B=¬A+¬B|¬A+¬B=¬A¬B


AND ex: A1*B0 = X0
OR ex: A1+B0 = X1
NAND ex: 1*0 = X0 negado ->1 resultado
NOR ex: 1+0 =  X0 negado -> 1 Res


Tabela Verdade AND        Tabela Verdade NAND
A|B|X|A¬B  x(saida)           A|B|X  x(saida)
0|0|0|0                     0|0|1
0|1|0|0                     0|1|1
1|0|0|1                     1|0|1
1|1|1|0                     1|1|0

Tabela Verdade OR         Tabela Verdade NOR
A|B|X  x(saida)           A|B|X  x(saida)
0|0|0                     0|0|1
0|1|1                     0|1|0
1|0|1                     1|0|0
1|1|1                     1|1|0

Tabela Verdade XOR         Tabela Verdade XNOR
A|B|X  x(saida)           A|B|X  x(saida)
0|0|0                     0|0|1
0|1|1                     0|1|0
1|0|1                     1|0|0
1|1|0                     1|1|0
XOR(Só um lado pode ser verdadeiro AKA 1)

ABCD
0000 1
0001 1 
0010 2 
0011 3
0100 4
0101 5
0110 6
0111 7
1000 8
1001 9
1010 10
1011 11
1100 12
1101 13
1110 14
1111 15

Y = XOR (A,B) = Aº+B =¬AB +A¬B??????
"""