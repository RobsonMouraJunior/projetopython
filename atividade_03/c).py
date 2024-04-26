#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 24/04/2024

#Importando as bibliotecas 
import os 


#Limpando o terminal 
os.system('cls')


print('-'*70)
print('Estudo de Condicional: Operadores logico')
print('='*70)
#entrada
velocidade = float(input("Digite a velocidade do carro em km/h: "))

limite_velocidade = 60  # Limite de velocidade em km/h

if velocidade <= limite_velocidade:
    print("Você está dentro do limite de velocidade.")
else:
    print("Atenção! Você ultrapassou o limite de velocidade de 60 km/h.")