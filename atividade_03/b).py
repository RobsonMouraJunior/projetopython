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
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
 
 #condicional
if a == b == c:
    print("Os números são todos iguais.")
else:
    maior = a
    menor = a

    if b > maior:
        maior = b
    elif b < menor:
        menor = b

    if c > maior:
        maior = c
    elif c < menor:
        menor = c

    print(f"O maior número é {maior}.")
    print(f"O menor número é {menor}.")