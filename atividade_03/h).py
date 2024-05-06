#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 28/04/2024

#Importando as bibliotecas 
import os 


#Importando as bibliotecas 
os.system('cls') 

print('-'*70)
print('Estudo de Condicional: Operadores lógicos')
print('='*70)

# Coeficientes da equação quadrática ax^2 + bx + c
a = 1
b = -6
c = 5

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica se o discriminante é positivo, negativo ou zero
if delta > 0:
    # Calcula as raízes reais distintas usando a fórmula de Bhaskara
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("As raízes da equação quadrática são:")
    print("x' =", x1)
    print("x'' =", x2)
elif delta == 0:
    # Calcula a raiz real única quando o discriminante é zero
    x = -b / (2*a)
    print("A equação quadrática tem uma raiz real única:")
    print("x =", x)
else:
    # Não existem raízes reais quando o discriminante é negativo
    print("A equação quadrática não possui raízes reais.")

#saida
