print('========== DESAFIO 033 ==========')
num1 = int(input('Digite 3 números:\n1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))

if num3 < num1 > num2:
    maior = num1
    print('\nMaior número digitado: {}'.format(maior))
elif num1 < num2 > num3:
    maior = num2
    print('\nMaior número digitado: {}'.format(maior))
elif num1 < num3 > num2:
    maior = num3
    print('\nMaior número digitado: {}'.format(maior))
else:
    print('\nOs números digitados são iguais.')


if num3 > num1 < num2:
    menor = num1
    print('Menor número digitado: {}'.format(menor))
elif num1 > num2 < num3:
    menor = num2
    print('Menor número digitado: {}'.format(menor))
elif num1 > num3 < num2:
    menor = num3
    print('Menor número digitado: {}'.format(menor))
    