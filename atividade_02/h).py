#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 19/04/2024
#atividade D

# Importando as bibliotecas
import os

# Biblioteca para data e hora do sistema
import datetime

# Limpar o terminal
os.system('cls')

print('-' * 70)
print('=' * 70)

# Recebe o número 
numero = int(input("Digite numero: "))

# Calcula o sucessor e antecessor
tabuada_0 = numero * 0
tabuada_1 = numero* 1
tabuada_2 = numero * 2
tabuada_3 = numero * 3
tabuada_4 = numero * 4
tabuada_5 = numero * 5
tabuada_6 = numero * 6
tabuada_7 = numero * 7
tabuada_8 = numero * 8
tabuada_9 = numero * 9
tabuada_10 = numero * 10

# Exibe o sucessor e antecessor na tela
# Exibe a tabuada na tela
print(f"Tabuada de {numero}:")
print(f"{numero} x 0 = {tabuada_0}")
print(f"{numero} x 1 = {tabuada_1}")
print(f"{numero} x 2 = {tabuada_2}")
print(f"{numero} x 3 = {tabuada_3}")
print(f"{numero} x 4 = {tabuada_4}")
print(f"{numero} x 5 = {tabuada_5}")
print(f"{numero} x 6 = {tabuada_6}")
print(f"{numero} x 7 = {tabuada_7}")
print(f"{numero} x 8 = {tabuada_8}")
print(f"{numero} x 9 = {tabuada_9}")
print(f"{numero} x 10 = {tabuada_10}")

print('-' * 70)