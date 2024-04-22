#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 12/04/2024
#primeiro programa em python

#Importando as bibliotecas 
import os 


# biblioteca para data e hora do sistema
import datetime


#limapando terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)

#entrada
nome = input('Entre com um nome:')

#Entrada com casting
nascimento = int(input('Data de nascimento:'))
cpf = str(input('Entre com o cpf:'))
altura = str(input('Entre com altura:'))
estudande = input('É estudante:') 


#saida
print('-'*70)
print('SAIDA DE DADOS')
print(f'nome...............:{nome}, ')
print(f'nascimento...............:{nascimento}')
print(f'altura...............:{altura}')
print(f'estudande...............:{estudande}')
