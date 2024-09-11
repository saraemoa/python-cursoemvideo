from random import randint
from time import sleep
print('========== DESAFIO 045 ==========')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
jogador = int(input("""1 - Pedra
2 - Papel
3 - Tesoura
\nO que deseja jogar? """))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if jogador == 1 or jogador == 2 or jogador == 3:
    print('\n', '=-' * 20)
    print("""O jogador jogou {}
    O computador jogou {}""".format(itens[jogador - 1], itens[computador - 1]))
    print('=-' * 20, '\n')
else:
    print('\nJOGADA INVÁLIDA!')

if jogador == computador:
    print('\nEMPATE!')
elif jogador == 1 and computador == 3:
    print('\nO JOGADOR VENCEU!')
elif computador == 1 and jogador == 3:
    print('\nO COMPUTADOR VENCEU!')
elif jogador == 1 and computador == 2:
    print('\nO COMPUTADOR VENCEU!')
elif computador == 1 and jogador == 2:
    print('\nO JOGADOR VENCEU!')
elif jogador == 2 and computador == 3:
    print('\nO COMPUTADOR VENCEU!')
elif computador == 2 and jogador == 3:
    print('\nO JOGADOR VENCEU!')
