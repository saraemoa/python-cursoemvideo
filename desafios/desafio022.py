print('========== DESAFIO 022 ==========')
nome = str(input('Digite seu nome completo: ')).strip()
print('Em letras maiúsculas: {}'.format(nome.upper()))
print('Em letras minúsculas: {}'.format(nome.lower()))
print('Possui {} letras no total.'.format(len(nome) - nome.count(' ')))
separado = nome.split()
print('Seu primeiro nome é: {}'.format(separado[0]))

