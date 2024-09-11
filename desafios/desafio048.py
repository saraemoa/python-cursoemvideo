print('=' * 10, ' DESAFIO 048 ', '=' * 10)
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('Soma dos múltiplos de 3 presentes entre 1 e 500:', soma)
