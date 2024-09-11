print('========== DESAFIO 028 ==========')
from random import randint
randNum = randint(0, 5)
usuarioNum = int(input('Escolha um número de 0 a 5: '))

if usuarioNum == randNum:
    print('GANHOU! O número pensado pelo computador foi o mesmo que você escolheu.')
else: 
    print('PERDEU! O número pensado pelo computador é diferente do que você escolheu.')