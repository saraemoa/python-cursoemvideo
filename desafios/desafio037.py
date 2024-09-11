print('========== DESAFIO 037 ==========')
print('''1 - Binário
2 - Octal
3 - Hexadecimal''')
escolha = int(input('Qual opção de conversão que deseja? '))
if escolha == 1: 
    num = int(input('\nQual o número que deseja converter? '))
    conversao = bin(num)
    print(f'O número {num} convertido em binário é {conversao}')
elif escolha == 2:
    num = int(input('\nQual o número que deseja converter? '))
    conversao = oct(num)
    print(f'O número {num} convertido em octal é {conversao}')
elif escolha == 3:
    num = int(input('\nQual o número que deseja converter? '))
    conversao = hex(num)
    print(f'O número {num} convertido em hexadecimal é {conversao}')
else:
    print('Opção inválida. Tente novamente')