
# biblioteca para interagir o SO
import os
# biblioteca para data e hora do sistema 
import datetime 


#limapando terminal
os.system('cls')

print('-'*70)
print('saida de dados')
print('='*70)




# Vamos supor uma taxa de câmbio de 5 reais para 1 dólar
taxa_de_cambio = 5

# Solicitando o valor em reais ao usuário
valor_em_reais = float(input("Digite o valor em reais: "))

# Calculando quantos dólares o valor em reais representa
valor_em_dolares = valor_em_reais / taxa_de_cambio

# Exibindo o resultado
print(f"Com {valor_em_reais} reais, você pode comprar {valor_em_dolares} dólares.")