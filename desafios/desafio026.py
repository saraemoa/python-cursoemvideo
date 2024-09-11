print('========== DESAFIO 026 ==========')
frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {}x na frase digitada.'.format(frase.lower().count('a')))
print('Aparece a 1ª vez no caracter {} e a última vez no caracter {}'.format(frase.lower().find('a'),frase.lower().rfind('a')))