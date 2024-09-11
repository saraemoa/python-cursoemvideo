print('========== DESAFIO 029 ==========')
velocidade = int(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você excedeu o limite máximo de velocidade e foi MULTADO.\nEm decorrência disso, deverá pagar R$ {:.2f}.'.format(multa))
else:
    print('PARABÉNS! Você estava dentro do limite máximo de velocidade.')