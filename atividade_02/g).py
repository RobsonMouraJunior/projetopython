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
metros = int(input("Digite medidas em metros: "))

# Calcula o sucessor e antecessor
centimetro = metros * 100
milimetro = metros * 1000

# Exibe o sucessor e antecessor na tela
print(f"{metros} equivalem a {centimetro}  é: centimetros.")
print(f"{metros} equivalem a {milimetro} é: milimetro")

print('-' * 70)
print('=' * 70)