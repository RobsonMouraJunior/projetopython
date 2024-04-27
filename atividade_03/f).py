#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 24/04/2024

#Importando as bibliotecas 
import os 


#Limpando o terminal 
os.system('cls')
print('-'*70)
print('Estudo de Condicional: Operadores lógicos')
print('='*70)

#entrada
ano = int(input('Digite um ano de número inteiro:'))
resposta = ''

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

# Saída
print(resposta)
print('='*70)
print('Fim do programa!\n')