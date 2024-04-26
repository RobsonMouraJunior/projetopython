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
c = 'josé'
d = 'josé'

print('-'*70)
print('Estudo de Condicional: Operadores Relacionais')
print('='*70)

 # Igaldade (==)
if c == d:
    print('-'*70)
    print(f'{c} é igual {d}')
    print('-'*70)
else:
    print(f'{a} não é igual a {b}') 

#diferente
if a != c:
    print('-'*70)      
    print(f'{a} é diferente de {c}')
    print('='*70)

# á maior que (>)
if a > b:
    print('-'*70)
    print(f'{a} é maior que {b}')
    print('='*70)
else:
    print(f'{a} é maior que {b}')

# Menor que (<)
if a < b:
    print('-'*70)
    print(f'{a} é menor que {b}')
    print('=')
else:
    print(f'{a} é menor que {b}')  

# Maior ou igual a (>=)    
if a >= b:
    print('-'*70)
    print(f'{a} é maior ou igual a {b}')
    print('='*70)
else:
    print(f'{a} é maior ou igual a {b}')
# Menor igual a (=<)    
if a <= b:
    print('-'*70)
    print(f'{a} é menor ou igual a {b}')
    print('='*70)
else:
    print(f'{a} é menor ou igual a {b}')
print('Fim do pograma')
print('-'*70)
print()    