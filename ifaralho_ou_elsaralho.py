# 4. Descubra se o número gosta de pares ou de fazer drama sendo ímpar
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("Par. Sério, tão estável quanto uma planilha do Excel.")
else:
    print("Ímpar. Com certeza faria um podcast só pra reclamar da vida.")

# 10. Esse número está entre 10 e 20 ou ele é um fora da curva?
n = int(input("Digite um número: "))
if 10 < n < 20:
    print("Está entre 10 e 20. Um número equilibrado, centrado, faz yoga.")
else:
    print("Fora do intervalo. Rebelde sem causa.")

# 14. Número negativo ou só tá tendo um dia ruim?
n = int(input("Digite um número: "))
if n < 0 or n < -10:
    print("Negativo ou abaixo de -10. Vai precisar de uma terapia de números inteiros.")
else:
    print("Está de boas... por enquanto.")

# 22. Negativo e ímpar. Provavelmente ouve músicas tristes de madrugada.
n = int(input("Digite um número: "))
if n < 0 and n % 2 != 0:
    print("Negativo e ímpar. Drama em dobro.")
else:
    print("Ou é positivo ou tem parcerias. Respeitável.")

# 28. Adulto: aquele limbo entre boletos e coluna travada
idade = int(input("Digite a idade: "))
if 18 <= idade <= 64:
    print("Adulto. Parabéns, agora você vive para pagar boletos.")
else:
    print("Ou ainda é jovem e sonhador, ou já atingiu o modo 'vou dormir às 20h'.")

# 36. Multiplicação explosiva
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a * b > 100:
    print("Multiplicação maior que 100. Isso sim é potência de fogo!")
else:
    print("Resultado tímido. Precisa de um empurrãozinho.")

# 56. Positivo, múltiplo de 3, mas não de 5. O diferentão.
n = int(input("Digite um número: "))
if n > 0 and n % 3 == 0 and n % 5 != 0:
    print("Esse aí gosta de seguir modinhas... mas não todas.")
else:
    print("Ou não é positivo, ou se vendeu pra todos os múltiplos possíveis.")

# 77. Múltiplo de 3 ou 5, mas não de 7. Escolheu lados na treta dos números.
n = int(input("Digite um número: "))
if (n % 3 == 0 or n % 5 == 0) and n % 7 != 0:
    print("É de um grupinho, mas evita o número 7. Panelinha detected.")
else:
    print("Ou é neutro, ou faz parte do time dos 7... estranho.")

# 90. Divisível por 3 e 5. Equilíbrio raro em tempos de polarização numérica.
n = int(input("Digite um número: "))
if n % 3 == 0 and n % 5 == 0:
    print("Esse número sabe agradar todo mundo.")
else:
    print("Meio indeciso ainda... precisa conversar com os múltiplos.")

# 100. Soma zero. A verdadeira definição de “empate técnico”.
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a + b == 0:
    print("Soma igual a zero. É tipo um casal que se cancela.")
else:
    print("Ainda resta alguma coisa aí. Nem que seja o troco.")
    
