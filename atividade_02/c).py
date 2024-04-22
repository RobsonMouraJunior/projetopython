# import
# biblioteca para interagir o SO
import os


# limapando terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)

# entrada de dados
nota_1 = float(input('Entre com a 1º nota:'))
nota_2 = float(input('Entre com a  2º nota:'))
nota_3 = float(input('Entre com a  3º nota:'))
nota_4 = float(input('Entre com a  4º nota:'))

# processamento
soma = nota_1 + nota_2 + nota_3 + nota_4
media = (nota_1 + nota_2 + nota_3 + nota_4)/4

# saida polarizada
print('saida de dados')
print('='*70)
 #saida 
print(f' a Soma da {nota_1} + {nota_2} + {nota_3} + {nota_4} é: {soma} ')
print(f'media das turma  é:{media}')

