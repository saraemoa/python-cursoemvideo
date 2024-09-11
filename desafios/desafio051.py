print('=' * 10, ' DESAFIO 051 ', '=' * 10)
termo = int(input('Digite o 1º termo da progressão aritmética: '))
razao = int(input('Digite a razão dessa progressão aritmética: '))
for i in range(1, 11):
    print(termo, end = " ") # o comando 'end = " "' faz com que todos os prints sejam colocados na mesma linha
    termo += razao