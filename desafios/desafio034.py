print('========== DESAFIO 034 ==========')
salario = float(input('Digite seu salário: '))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print('Você recebeu um aumento de 10%.\nSeu novo salário é de R$ {}'.format(aumento))
else:
    aumento = salario * 1.15
    print('Você recebeu um aumento de 15%.\nSeu novo salário é de R$ {}'.format(aumento))
