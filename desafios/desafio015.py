print('========== DESAFIO 015 ==========')
dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos km o carro percorreu: '))
total = 60 * dias + 0.15 * km
print('O total a pagar será de R$ {}.'.format(total))