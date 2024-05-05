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


# entrada_Coeficientes da equação quadrática ax^2 + bx + c
a = 1
b = -6
c = 5

# Calcula as raízes usando a fórmula de Bhaskara
x1 = (b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (b - (b**2 - 4*a*c)**0.5) / (2*a)

# Imprime as raízes calculadas
print("As raízes da equação quadrática são:")
print("x' =", x1)
print("x'' =", x2)