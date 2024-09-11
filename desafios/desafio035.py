print('========== DESAFIO 035 ==========')
reta1 = int(input('Informe o valor das 3 retas:\n1ª reta: '))
reta2 = int(input('2ª reta: '))
reta3 = int(input('3ª reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
    
