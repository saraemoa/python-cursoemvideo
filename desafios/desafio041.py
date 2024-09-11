from datetime import date
print('========== DESAFIO 041 ==========')
anoNascimento = int(input('Digite o ano de nascimento do(a) atleta: '))
anoAtual = int(input('Informe o ano atual: '))
#anoAtual = date.today().year - função para pegar o ano da data atual
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')