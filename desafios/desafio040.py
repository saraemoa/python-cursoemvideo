print('========== DESAFIO 040 ==========')
nota1 = float(input('Informe a 1ª nota do(a) aluno(a): '))
nota2 = float(input('Informe a 2ª nota do(a) aluno(a): '))
media = (nota1 + nota2) / 2
if media < 5:
    print('O(a) aluno(a) foi REPROVADO.')
elif media >= 5:
    print('O(a) aluno(a) está de RECUPERAÇÃO.')
elif media >= 7:
    print('O(a) aluno foi APROVADO.')