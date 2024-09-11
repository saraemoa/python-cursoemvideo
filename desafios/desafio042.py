print('========== DESAFIO 042 ==========')
reta1 = int(input('Informe o valor das 3 retas:\n1ª reta: '))
reta2 = int(input('2ª reta: '))
reta3 = int(input('3ª reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 == reta3:
        print('É possível formar um triângulo EQUILÁTERO, ou seja, um triângulo que possui todos os lados iguais.')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('É possível formar um triângulo ISÓSCELES, ou seja, um triângulo que possui 2 apenas lados iguais.')
    elif reta1 != reta2 != reta3 != reta1:
        print('É possível formar um triângulo ESCALENO, ou seja, um triângulo que possui todos os lados diferentes.')
else:
    print('Não é possível formar um triângulo com essas retas.')
    