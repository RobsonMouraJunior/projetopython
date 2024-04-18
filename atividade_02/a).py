# imports
import os

# linear o terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)

# entrada de dados
parcela_1 = float(input('Entre com a 1º parcela:'))
parcela_2 = float(input('Entre com a  2º parcela'))
parcela_3 = float(input('Entre com a  3º parcela'))

multiplicando_1 = float(input('Entre com  o multiplicado'))
multiplicando_2 = float(input('Entre com  o multiplicado'))
multiplicando_3 = float(input('Entre com  o multiplicado'))
# processamento
soma = parcela_1 + parcela_2 + parcela_3
produto = multiplicando_1 * multiplicando_2 * multiplicando_3
# saida polarizada1
print('saida de dados')
print('='*70)

print(f' a Soma da {parcela_1} + {parcela_2} + {parcela_3} é: {soma}')
print(f' a multiplicação da {multiplicando_1} * {multiplicando_2} *1 {multiplicando_3} é: {produto}')