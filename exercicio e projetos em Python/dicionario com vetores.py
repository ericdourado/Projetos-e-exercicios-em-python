'''
Considere o dicionário:
D = {‘a’: [1, 3, 5, 7], ‘b’: [2, 4, 6, 8], ‘c’: [9, 10, 11, 12]}
3.1 – Crie um algoritmo que some todos os valores do dicionário.
'''

D = {'a':[1, 3, 5, 7],
     'b':[2, 4, 6, 8],
     'c':[9, 10, 11, 12]
     }
soma = 0

for k,v in D.items():      # k= keys /  v = valores
    for x in v:
        soma += x


print(f'A soma de todos valores é {soma}')


