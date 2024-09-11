print('========== DESAFIO 031 ==========')
distancia = int(input('Qual a distância até o destino desejado? '))
if distancia < 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O valor da passagem é de R$ {:.2f}'.format(passagem))
