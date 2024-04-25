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

#entrada
<<<<<<< HEAD
valor = int(input('Digite um número decimal:'))
resposta = ''

#condicional
if valor % 2 == 0:
    valor-int(valor)
=======
valor = float(input('Digite um número decimal:'))
resposta = ''

#condicional
if valor % 1 == 0: 
>>>>>>> 2811b3a7a793a31e37a80be0985ac84154ad4a1c
    resposta = f'Entrada incorreta, o valor {valor} é um inteiro!'
else:
    resposta = f'Entrada  correta, o valor {valor} é um decimal'   

 #saida
print('='*70)
print(resposta)

print('Fim do programa!\n') #\n salta uma linha