#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 24/04/2024

#Importando as bibliotecas 
import os 


os.system('cls')

#declarações
a = 10
b = 5
resposta = ''

print('-'*70)
print('Estudo de Condicional (simples)')
print('='*70)

#condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:   
    resposta = f'{a} não é maior que {b}'
#saida
print('-'*70) 
print(resposta)

#declarações
a = 5
b = 5

print('-'*70)
print('Estudo de Condicional (aninhada)')
print('='*70)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b: 
    resposta = f'{a} é menor que {b}' 
else:
    resposta = f'O valor são iguasi: {a} = {b}'
    
print('-'*70)
print(resposta)
print('-'*70)
print()
           