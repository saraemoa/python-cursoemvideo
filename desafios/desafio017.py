print('========== DESAFIO 017 ==========')
from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente) # OU hipotenusa = sqrt(oposto**2 + adjacente**2)
print('A hipotenusa desse triângulo tem {:.2f} cm de comprimento.'.format(hipotenusa))