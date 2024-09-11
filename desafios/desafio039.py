print('========== DESAFIO 039 ==========')
anoNascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = int(input('Informe o ano atual: '))
idade = anoAtual - anoNascimento
if idade < 18:
    prazo = 18 - idade
    print('Você ainda vai se alistar ao serviço militar.\nFalta(m) {} ano(s) para o seu alistamento.'.format(prazo))
elif idade == 18:
    print('É a hora de alistar ao serviço militar.')
else:
    prazo = idade - 18
    print('Já passou do tempo de realizar o alistamento ao serviço militar.\nExiste {} ano(s) de atraso.'.format(prazo))