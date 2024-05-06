#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 28/04/2024

#Importando as bibliotecas 
import os 


#Limpando o terminal 
os.system('cls')
print('-'*70)
print('Estudo de Condicional: Operadores lógicos')
print('='*70)

#Entrada
seg_1 = float(input('Digite a médida de um segmento de triangulo:'))
seg_2 = float(input('Digite a médida de um segmento de triangulo:'))
seg_3 = float(input('Digite a médida de um segmento de triangulo:'))
resposta = ''

#proceso
if  seg_1 + seg_2 > seg_3 and seg_2 + seg_3 > seg_1 and seg_1 + seg_3 > seg_2:
    print('Os 3 segmentos formam um triangulo')
else:
    print('Os segmentos não formam um triangulo')

# Saída
print('-'*70)
print(resposta)
print('='*70)
print('Fim do programa!\n')
