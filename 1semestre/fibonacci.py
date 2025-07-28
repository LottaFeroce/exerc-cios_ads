import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função para gerar a sequência de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Número de elementos da sequência Fibonacci a ser exibido
n = 20

# Gerar sequência de Fibonacci
fib_sequence = fibonacci(n)

# Preparar a figura
fig, ax = plt.subplots()
ax.set_xlim(0, n-1)
ax.set_ylim(0, max(fib_sequence) + 5)
line, = ax.plot([], [], 'r-', lw=2)

# Função de inicialização da animação
def init():
    line.set_data([], [])
    return line,

# Função para atualizar os dados da animação
def update(frame):
    x_data = np.arange(frame)
    y_data = fib_sequence[:frame]
    line.set_data(x_data, y_data)
    return line,

# Criar a animação
ani = FuncAnimation(fig, update, frames=n, init_func=init, blit=True, interval=500)

plt.title('Animação da Sequência de Fibonacci')
plt.xlabel('Índice')
plt.ylabel('Valor de Fibonacci')
plt.show()
