print('========== DESAFIO 004 ==========')
algo = input('Digite algo: ')
print(type(algo))
print('O termo digitado é alfabético? {0}'.format(algo.isalpha()))
print('O termo digitado é numérico? {0}'.format(algo.isnumeric()))
print('O termo digitado é alfabético e/ou numérico? {0}'.format(algo.isalnum()))
print('O termo digitado é maiúsculo? {0}'.format(algo.isupper()))
print('O termo digitado é minúsculo? {0}'.format(algo.islower()))
print('O termo digitado é decimal? {0}'.format(algo.isdecimal()))
print('O termo digitado é título, ou seja, tem a primeira letra de cada palavra maiúscula? {0}'.format(algo.istitle()))