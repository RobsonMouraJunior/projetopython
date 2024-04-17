#import
# biblioteca para interagir o SO
import os
# biblioteca para data e hora do sistema 
import datetime 


#limapando terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)

#entrada
nome = input('entre com um nome: ')
nome = input(' entre com o peso: ')
nome = input('Entre com a altura: ')

#Entrada com Casting
nascimento = int(input('data de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = int(input('entre com o bairro: '))
rua = int(input('nome da rua: '))
nnumero = int(input('Entre com o numero: '))

#Processamento: pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

#Saida 
print('-'*70)
print('saida de dados')
print('='*70)
print('nome...............: ', nome)
print('data de nascimento...............: ', 2006)
print('peso...............: ',80)
print('altura...............: ', 1.85)

#Saida Intrpolada 
print(f'{nome}, você tem {idade} anos!')
print(f'cep...............: {cep}')
print(f'bairro...............: {bairro}')
print(f'rua...............:  {rua}')
print(f'Numero...............:  {nnumero}')
print('-'*70)
print('')
