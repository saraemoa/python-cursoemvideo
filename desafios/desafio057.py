print('=' * 10, ' DESAFIO 057 ', '=' * 10)
while True:
    sexo = str(input('Digite seu sexo: ')).upper().strip()
    if sexo != 'F' and sexo != 'M':
        print('Sexo inválido. Tente novamente.')
    else:
        print('Sexo válido.')
        break