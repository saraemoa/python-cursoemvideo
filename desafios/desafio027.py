print('========== DESAFIO 027 ==========')
nome = str(input('Digite seu nome completo: '))
separado = nome.split()
print("""Primeiro nome: {}
Último nome: {}""".format(separado[0], separado[len(separado)-1]))