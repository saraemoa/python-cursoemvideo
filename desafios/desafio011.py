print('========== DESAFIO 011 ==========')
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
tinta = area/2
print('Para pintar uma parede de {} m² será(ão) necessário(s) {} litro(s) de tinta'.format(area, tinta))