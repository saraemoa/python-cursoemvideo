print('========== DESAFIO 018 ==========')
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
angulo = radians(angulo) #convertendo para radianos, pois o parâmetro das funções usadas abaixo estão em radianos
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(angulo), cos(angulo), tan(angulo)))
