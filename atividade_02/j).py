# import
# biblioteca para interagir o SO
import os


# limapando terminal
os.system('cls')

print('-'*70)
print('='*70)

#entrada
lado_1 = float(input('Entre com o lado 1:'))
lado_2= float(input('Entre com o lado 2:'))

#procesamento
resultado = (lado_1 * 2) + (lado_2 * 2)

#saida
print('-'*70)
print('saida de dados')
print(f' a Soma das bases dos lados é {resultado} :')
print('-'*70)
print('='*70)