#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 24/04/2024

#Importando as bibliotecas 
import os 


#Limpando o terminal 
os.system('cls')


print('-'*70)
print('Estudo de Condicional: Parte 1')
print('='*70)

numero = int(input('Digite um número inteiro:'))
resposta = ''

#condicional
print('verificação se e Par ou Impar')
if numero % 2 == 0: 
    resposta = f'O número {numero} é par!'
else:
    resposta = f'O número {numero} é impar'      
 
#saida
print('='*70)
print(resposta)

print('Fim do programa!\n') #\n salta uma linha    