print('========== DESAFIO 036 ==========')
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos você deseja pagar essa casa? '))
prestacao = casa / (anos * 12)
if prestacao <= salario * 0.3:
    print('\nEmpréstimo recusado. O valor da prestação excede o valor de 30% do seu salário.')
else:
    print('\nEmpréstimo aprovado.')