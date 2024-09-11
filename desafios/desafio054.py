from datetime import date
print('=' * 10, ' DESAFIO 054 ', '=' * 10)
menoresDeIdade = 0
maioresDeIdade = 0
print('Informe o ano de nascimento de 7 pessoas:')
for i in range(1, 8):
    ano = int(input(f'Pessoa {i}: '))
    if date.today().year - ano < 21:
        menoresDeIdade += 1
    else:
        maioresDeIdade += 1
print(f'Dentre as pessoas digitadas, existem {maioresDeIdade} maiores de idade e {menoresDeIdade} menores de idade.')