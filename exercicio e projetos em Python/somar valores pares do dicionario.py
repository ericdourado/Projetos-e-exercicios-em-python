'''
3.3 – Crie um algoritmo que some os valores pares do dicionários.

'''

dicionario = {'a':1, 'b':2, 'c':3, 'd':-1, 'e':-3, 'f':6, 'g':4}
soma = 0
for chave in dicionario:
    if dicionario[chave] % 2 == 0:
        soma += dicionario[chave]
print(f'A soma dos numeros pares é: {soma}')

