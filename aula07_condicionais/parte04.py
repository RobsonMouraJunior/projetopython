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

print('-'*70)
print('Estudo de Condicional: Operadores logico')
print('='*70)

#E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('verdadeiro: bloco executado')
else:
    print('Falso: Bloco executado')    

print('.'*70)
#E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: bloco executado')    

print('.'*70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO') 
if ( a > 5 or b == c):
    print('VERDADEIRO: Bloco executado')
else:
    print('Falso: Bloco executado')   

print('-'*70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'jane'):
    print('Falso: Bloco executado')
else:
    print('Falso: Bloco executado')    
print('-'*70)  
print()  