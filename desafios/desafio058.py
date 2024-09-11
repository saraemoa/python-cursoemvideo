from random import randint
print('=' * 10, ' DESAFIO 058 ', '=' * 10)
tentativa = 1
randNum = randint(0, 10)
while True:
    usuarioNum = int(input('Escolha um número de 0 a 10: '))

    if usuarioNum == randNum:
        print('GANHOU! O número pensado pelo computador foi o mesmo que você escolheu.')
        print(f'Você precisou de {tentativa} tentativa(s) para acertar.')
        break
    else:
        tentativa += 1
        print('ERRADO! Tente mais uma vez.')