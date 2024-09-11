print('========== DESAFIO 024 ==========')
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade digitada começa com a palavra "Santo"?', 'SANTO' in cidade[:5].upper())
# retorna -1 para falso e o caracter onde ele inicia para verdadeiro