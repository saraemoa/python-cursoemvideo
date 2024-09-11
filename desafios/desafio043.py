print('========== DESAFIO 043 ==========')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu status é: ABAIXO DO PESO')
elif imc < 25:
    print('Seu status é: PESO IDEAL')
elif imc < 30:
    print('Seu status é: SOBREPESO')
elif imc < 40:
    print('Seu status é: OBESIDADE')
else:
    print('Seu status é: OBESIDADE MÓRBIDA')