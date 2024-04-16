#imporatando a biblioteca
import os


#limapando terminal
os.system('cls')

print('-'*70)
print('Estudos de variaveis')
print('='*70)

# As varoavei são declaradas por inferencia
nome = 'Jhon Done'
nascimento = 1970
altura = 1.80
peso = 75.5
doador = True
complexo = 3j # python trabalha diretamente  com numeros complexos
PI = 3.14 # isso e uma CONSTANTE, seu valor nao deve ser alterado

#Saida utilizando o metodo type() para verificar o ________________________________________________
#tipo da variavel 
print('\033[0m \033[31mtipos declarados;\033[0m')
print('\033[0m A var \033[32m nome \033[0m é do tipo: ', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m é do tipo: ', type(nascimento))
print('\033[0m A var \033[32m altura \033[0m é do tipo: ', type(altura))
print('\033[0m A var \033[32m peso \033[0m é do tipo: ', type(peso))
print('\033[0m A var \033[32m doador\033[0m é do tipo: ', type(doador))
print('\033[0m A var \033[32m complexo \033[0m é do tipo: ', type(complexo))
print('\033[0m A var \033[32m PI\033[0m é do tipo: ', type(PI))
print('-'*70)
print('')