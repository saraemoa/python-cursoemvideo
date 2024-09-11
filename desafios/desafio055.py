print('=' * 10, ' DESAFIO 055 ', '=' * 10)
maiorPeso = 0
print('Informe o peso de 5 pessoas: ')
for i in range(1, 6):
    peso = float(input(f'Peso da pessoa {i}: '))
    if i == 1:
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'Dentre os pesos digitados, o maior deles foi {maiorPeso} e o menor foi {menorPeso}.')