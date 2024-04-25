#curso de Desenvolvimento de Sistema
#Turma 0152 (braba)
#Autor: Robson Moura  
#Data: 24/04/2024

# biblioteca para interagir o SO
# limapando terminal
os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('='*70)

#entrada
valor = int(input('Digite um número decimal:'))
resposta = 'valor-int(valor)'

#condicional
if valor % 2 == 0:
    resposta = f'Entrada incorreta, o valor {valor} é um inteiro!'
else:
    resposta = f'Entrada  correta, o valor {valor} é um decimal'   

 #saida
print('='*70)
print(resposta)

print('Fim do programa!\n') #\n salta uma linha