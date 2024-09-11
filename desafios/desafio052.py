print('=' * 10, ' DESAFIO 052 ', '=' * 10)
divisores = 0
num = int(input('Digite um número inteiro: '))
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

if divisores != 2:
    print(f'O número {num} NÃO é primo.')
else:
    print(f'O número {num} É primo.')
