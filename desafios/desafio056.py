print('=' * 10, ' DESAFIO 056 ', '=' * 10)
somaIdade = 0
idadeHomemMaisVelho = 0
mulheresMenores20 = 0
print( 'Informe os seguintes dados de 4 pessoas: ')
for i in range(1, 5):
    print(f'===== {i}ª PESSOA =====')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    somaIdade += idade
    if sexo[0].lower() == 'm' and idade > idadeHomemMaisVelho:
        nomeHomemMaisVelho = nome
        idadeHomemMaisVelho = idade
    if sexo[0].lower() == 'f' and idade < 20:
        mulheresMenores20 += 1
print(f'Média de idade: {somaIdade/4}\nHomem mais velho: {nomeHomemMaisVelho}')
print(f'Mulheres menores de 20 anos: {mulheresMenores20}')
