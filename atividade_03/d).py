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

# Entrada 
salario_atual = float(input('Digite o salário mensal: '))
salario_baixo = 1000

# Processamento
aumento_5 = salario_atual * (1 + 5/100)
aumento_10 = salario_atual * (1 + 10/100)

if salario_atual > salario_baixo:
    resposta = f'Recebeu um aumento de {salario_atual} para {aumento_5:.2f}'
else:
    resposta = f'Recebeu um aumento de {salario_atual} para {aumento_10:.2f}'

# Saída
print(resposta)
print('='*70)
print('Fim do programa!\n')