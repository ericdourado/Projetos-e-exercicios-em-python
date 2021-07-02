'''
3.4 – Crie um algoritmo que some os valores negativos do dicionário.
'''
lista_d = list()
D = {'a':[1, 3, 5, 7],
     'b':[2, 4, 6, 8],
     'c':[9, 10, 11, 12]
     }

for contador in range(0,6):
    x = int(input(f'Digite um valor a ser adicionado no dicionario na letra "d": '))
    lista_d.append(x)
D['d'] = lista_d
print(D)
soma = 0

for c in D['d']:
    soma += c
print(f'A soma dos valores negativos do dicionário é: {soma}')

