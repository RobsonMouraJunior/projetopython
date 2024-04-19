#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 12/04/2024
#primeiro programa em python

#Importando as bibliotecas 
import os 

# biblioteca para data e hora do sistema
import datetime


# linear o terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)

print()
print('DIVISÃO')
print('='*70)

#entrada de dados
dividendo = float(input('Entre com o dividendo'))
divisor = float(input('Entre com o divisor'))

# Procesamento
quociente = dividendo/divisor

#saida
print(f'A divisão de {dividendo} / {divisor} é; {quociente}')