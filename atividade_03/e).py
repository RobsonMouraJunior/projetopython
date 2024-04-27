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
distancia=  float(input("Digite a distancia percorrida pelo  onibus em km/h: "))

if distancia <= 200:
    preco = distancia* 0.70
else:
    preco = distancia* 0.40

print(f'O preço da passagem é R${preco:.2f}')