print('=' * 10, ' DESAFIO 053 ', '=' * 10)
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
palavras = frase.split()
fraseSemEspaco = ''.join(palavras)
inverso = ''
for letra in range(len(fraseSemEspaco) - 1, -1, -1):
    inverso += fraseSemEspaco[letra]

print(f'Frase digitada: {frase.upper()}')
if inverso == fraseSemEspaco:
    print('A frase digitada É um palíndromo.')
else:
    print('A fase digitada NÃO é um palíndromo.')

