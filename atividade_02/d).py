#Data: 19/04/2024
#atividade D


# Importando as bibliotecas
import os


# Biblioteca para data e hora do sistema
import datetime


# Limpar o terminal
os.system('cls')


print()
print('DIVISÃO')
print('=' * 70)


# Entrada de dados
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))


# Processamento
resultado_divisao = dividendo / divisor


# Saída formatada com 4 casas decimais
print(f'A divisão de {dividendo} / {divisor} resultado é: {resultado_divisao:.4f}')


print('-' * 70)
print('=' * 70)