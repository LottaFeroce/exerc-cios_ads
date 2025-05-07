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
Associative law| (Slide passou)


AND ex: A1*B0 = X0
OR ex: A1+B0 = X1
NAND ex: 1*0 = X0 negado ->1 resultado
NOR ex: 1+0 =  X0 negado -> 1 Res


Tabela Verdade AND        Tabela Verdade NAND
A|B|X  x(saida)           A|B|X  x(saida)
0|0|0                     0|0|1b
0|1|0                     0|1|1
1|0|0                     1|0|1
1|1|1                     1|1|0

Tabela Verdade OR         Tabela Verdade NOR
A|B|X  x(saida)           A|B|X  x(saida)
0|0|0                     0|0|1
0|1|1                     0|1|0
1|0|1                     1|0|0
1|1|1                     1|1|0


"""