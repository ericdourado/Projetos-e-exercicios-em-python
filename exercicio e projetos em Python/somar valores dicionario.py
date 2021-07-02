'''
Considere o dicionário:
D = {‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’: -1, ‘e’: -3, ‘f’:6, ‘g’:4}
3.1 – Crie um algoritmo que some todos os valores do dicionário.

'''

dicionario = {'a':1, 'b':2, 'c':3, 'd':-1, 'e':-3, 'f':6, 'g':4}
soma = 0
for chave in dicionario:
    soma += dicionario[chave]
print(f'A soma dos elementos do dicionário é: {soma}')


