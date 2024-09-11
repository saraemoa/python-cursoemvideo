print('=' * 10, ' DESAFIO 050 ', '=' * 10)
soma = 0
print( 'Informe 6 números: ')
for i in range(1, 7):
    num = int(input(f'{i}º número: '))
    if num % 2 == 0:
        soma += num
print('Soma dos números pares digitados:', soma)