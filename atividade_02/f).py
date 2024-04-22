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
numero = int(input("Digite um número inteiro: "))

# Calcula o sucessor e antecessor
dobro = numero * 2
triplo = numero * 3

# Exibe o sucessor e antecessor na tela
print(f"O dobro de {numero} é: {dobro}")
print(f"O triplo de {numero} é: {triplo}")

print('-' * 70)
print('=' * 70)
